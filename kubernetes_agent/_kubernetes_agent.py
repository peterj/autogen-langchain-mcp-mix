import json
import subprocess
import traceback
from typing import Any, List, Optional, Sequence, Tuple

from autogen_agentchat.agents import BaseChatAgent
from autogen_agentchat.base import Response
from autogen_agentchat.messages import (
    ChatMessage,
    MultiModalMessage,
    TextMessage,
)
from autogen_core import CancellationToken, FunctionCall
from autogen_core.models import (
    AssistantMessage,
    ChatCompletionClient,
    LLMMessage,
    SystemMessage,
    UserMessage,
)

from kubernetes_agent._tool_definitions import  TOOL_GET_PODS


class KubernetesAgent(BaseChatAgent):
    DEFAULT_DESCRIPTION = "An agent that can handle executing Kubernetes CLI (kubectl) commands."

    DEFAULT_SYSTEM_MESSAGES = [
        SystemMessage(
            content="""
        You are a helpful AI Assistant.
        When given a user query, use available functions to help the user with their request."""
        ),
    ]

    def __init__(
        self,
        name: str,
        model_client: ChatCompletionClient,
        description: str = DEFAULT_DESCRIPTION,
    ) -> None:
        super().__init__(name, description)
        self._model_client = model_client
        self._chat_history: List[LLMMessage] = []


    @property
    def produced_message_types(self) -> Sequence[type[ChatMessage]]:
        return (TextMessage,)

    async def on_messages(self, messages: Sequence[ChatMessage], cancellation_token: CancellationToken) -> Response:
        """ This is where you have to handle the incoming message """
        
        # store the message in chat history
        for chat_message in messages:
            if isinstance(chat_message, TextMessage | MultiModalMessage):
                self._chat_history.append(UserMessage(content=chat_message.content, source=chat_message.source))
            else:
                raise ValueError(f"Unexpected message in KubernetesAgent: {chat_message}")

        try:
            _, content = await self._generate_reply(cancellation_token=cancellation_token)
            self._chat_history.append(AssistantMessage(content=content, source=self.name))
            return Response(chat_message=TextMessage(content=content, source=self.name))

        except BaseException:
            content = f"kubernetes agent error:\n\n{traceback.format_exc()}"
            self._chat_history.append(AssistantMessage(content=content, source=self.name))
            return Response(chat_message=TextMessage(content=content, source=self.name))

    async def on_reset(self, cancellation_token: CancellationToken) -> None:
        self._chat_history.clear()

    async def _generate_reply(self, cancellation_token: CancellationToken) -> Tuple[bool, str]:
        history = self._chat_history[0:-1]
        last_message = self._chat_history[-1]
        assert isinstance(last_message, UserMessage)

        task_content = last_message.content  # the last message from the sender is the task

        # kubectl_version = run_kubectl_command("version", ["--client", "--short"])

        # # TODO: This is where we could gather and provide any other context needed to run the task
        # context_message = UserMessage(
        #     source="user",
        #     content=f"Your kubectl version is '{kubectl_version}'.",
        # )

        task_message = UserMessage(
            source="user",
            content=task_content,
        )

        create_result = await self._model_client.create(
            messages=history + [task_message],
            tools=[
                TOOL_GET_PODS,
            ],
            cancellation_token=cancellation_token,
        )

        response = create_result.content

        if isinstance(response, str):
            # Answer directly.
            return False, response

        elif isinstance(response, list) and all(isinstance(item, FunctionCall) for item in response):
            function_calls = response
            for function_call in function_calls:
                tool_name = function_call.name

                try:
                    arguments = json.loads(function_call.arguments)
                except json.JSONDecodeError as e:
                    error_str = f"KubernetesAgent encountered an error decoding JSON arguments: {e}"
                    return False, error_str

                command_result = ""
                if tool_name == "get_pods":
                    command_result = run_kubectl_command("get", ["pods"], arguments)
                    return False, command_result

        final_response = "TERMINATE"
        return False, final_response
    



def format_kubectl_arg(key: str, value: Any) -> List[str]:
    """
    Format a single kubectl argument based on its type and value.
    Returns a list of command arguments.
    """
    if value is None or value == "":
        return []
        
    # Convert snake_case to kebab-case for kubectl
    key = key.replace('_', '-')
    
    # Handle boolean flags
    if isinstance(value, bool):
        return [f"--{key}"] if value else []
    
    # Handle array types (filename, label-columns)
    if isinstance(value, list):
        if not value:  # Empty list
            return []
        if key in ["filename", "label-columns"]:
            return [f"--{key}=" + ",".join(str(v) for v in value)]
        return sum([[f"--{key}", str(v)] for v in value], [])
    
    # Handle special cases for certain arguments
    if key == "output" and value:
        return ["-o", str(value)]
    
    # Handle standard key-value pairs
    return [f"--{key}={value}"]

def run_kubectl_command(command: str, arguments: List[str], raw_args: Optional[dict] = None) -> str:
    """
    Run a kubectl command with the given arguments and additional raw arguments.
    
    Args:
        command: The kubectl command (e.g., 'get')
        arguments: List of positional arguments
        raw_args: Dictionary of additional arguments to format
    
    Returns:
        Command output as string
    """
    try:
        base_command = ["kubectl", command] + arguments
        
        if raw_args:
            for key, value in raw_args.items():
                base_command.extend(format_kubectl_arg(key, value))
        
        result = subprocess.run(
            base_command,
            capture_output=True,
            text=True,
            check=True  # This will raise CalledProcessError if command fails
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        error_msg = f"Error running kubectl command: {e}\nStderr: {e.stderr}"
        raise RuntimeError(error_msg)
    except Exception as e:
        raise RuntimeError(f"Unexpected error running kubectl command: {e}")

def handle_get_pods(arguments: dict) -> tuple[bool, str]:
    """
    Handle the get_pods tool command with all possible arguments.
    
    Args:
        arguments: Dictionary of arguments from the ToolSchema
        
    Returns:
        Tuple of (success: bool, result: str)
    """
    try:
        # Base arguments for the get pods command
        base_args = ["pods"]
        
        # Handle namespace
        namespace = arguments.get("namespace", "default")
        if not arguments.get("all_namespaces"):
            base_args.extend(["-n", namespace])
            
        # Remove arguments that are handled separately
        kubectl_args = arguments.copy()
        kubectl_args.pop("namespace", None)
        
        # Handle filename/kustomize mutual exclusivity
        if kubectl_args.get("filename") and kubectl_args.get("kustomize"):
            return False, "Error: Cannot use both filename and kustomize options"
            
        # Run the command with all arguments
        result = run_kubectl_command("get", base_args, kubectl_args)
        return True, result
        
    except Exception as e:
        return False, str(e)