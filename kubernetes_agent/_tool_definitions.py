from autogen_core.tools import ParametersSchema, ToolSchema



TOOL_GET_PODS = ToolSchema(
    name="get_pods",
    description="Get's the pods from a specific namespace.",
    parameters=ParametersSchema(
        type="object",
        properties={
            "namespace": {
                "type": "string",
                "description": "The namespace to get pods from.",
            },
        },
        required=["namespace"],
    )
)
