from autogen_core.tools import ParametersSchema, ToolSchema



TOOL_GET_PODS = ToolSchema(
    name="get_pods",
    description="Display one or many pod resources. Prints a table of the most important information about the specified pods. You can filter the list using a label selector and the --selector flag.",
    parameters=ParametersSchema(
        type="object",
        properties={
            "namespace": {
                "type": "string",
                "description": "The namespace to get pods from.",
            },
            "all_namespaces": {
                "type": "boolean",
                "description": "If true, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.",
                "default": False
            },
            "allow_missing_template_keys": {
                "type": "boolean",
                "description": "If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.",
                "default": True
            },
            "chunk_size": {
                "type": "integer",
                "description": "Return large lists in chunks rather than all at once. Pass 0 to disable. This flag is beta.",
                "default": 500
            },
            "field_selector": {
                "type": "string",
                "description": "Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. key1=value1,key2=value2).",
                "default": ""
            },
            "filename": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Filename, directory, or URL to files identifying the resource to get from a server."
            },
            "ignore_not_found": {
                "type": "boolean",
                "description": "If the requested object does not exist the command will return exit code 0.",
                "default": False
            },
            "kustomize": {
                "type": "string",
                "description": "Process the kustomization directory. This flag can't be used together with filename or recursive.",
                "default": ""
            },
            "label_columns": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Accepts a comma separated list of labels that are going to be presented as columns. Names are case-sensitive."
            },
            "no_headers": {
                "type": "boolean",
                "description": "When using the default or custom-column output format, don't print headers.",
                "default": False
            },
            "output": {
                "type": "string",
                "description": "Output format. One of: json, yaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file, custom-columns, custom-columns-file, wide",
                "enum": [
                    "json",
                    "yaml",
                    "name",
                    "go-template",
                    "go-template-file",
                    "template",
                    "templatefile",
                    "jsonpath",
                    "jsonpath-as-json",
                    "jsonpath-file",
                    "custom-columns",
                    "custom-columns-file",
                    "wide"
                ],
                "default": ""
            },
            "output_watch_events": {
                "type": "boolean",
                "description": "Output watch event objects when --watch or --watch-only is used.",
                "default": False
            },
            "raw": {
                "type": "string",
                "description": "Raw URI to request from the server. Uses the transport specified by the kubeconfig file.",
                "default": ""
            },
            "recursive": {
                "type": "boolean",
                "description": "Process the directory used in filename recursively.",
                "default": False
            },
            "selector": {
                "type": "string",
                "description": "Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. key1=value1,key2=value2)",
                "default": ""
            },
            "server_print": {
                "type": "boolean",
                "description": "If true, have the server return the appropriate table output. Supports extension APIs and CRDs.",
                "default": True
            },
            "show_kind": {
                "type": "boolean",
                "description": "If true, list the resource type for the requested object(s).",
                "default": False
            },
            "show_labels": {
                "type": "boolean",
                "description": "When printing, show all labels as the last column.",
                "default": False
            },
            "show_managed_fields": {
                "type": "boolean",
                "description": "If true, keep the managedFields when printing objects in JSON or YAML format.",
                "default": False
            },
            "sort_by": {
                "type": "string",
                "description": "If non-empty, sort list types using this field specification. The field specification is expressed as a JSONPath expression.",
                "default": ""
            },
            "subresource": {
                "type": "string",
                "description": "If specified, gets the subresource of the requested object. Must be one of [status scale].",
                "enum": ["status", "scale"],
                "default": ""
            },
            "template": {
                "type": "string",
                "description": "Template string or path to template file to use when -o=go-template, -o=go-template-file.",
                "default": ""
            },
            "watch": {
                "type": "boolean",
                "description": "After listing/getting the requested object, watch for changes.",
                "default": False
            },
            "watch_only": {
                "type": "boolean",
                "description": "Watch for changes to the requested object(s), without listing/getting first.",
                "default": False
            }
        },
        required=["namespace"]
    )
)


TOOL_GET_DEPLOYMENTS = ToolSchema(
    name="get_deployments",
    description="Display one or many deployment resources. Prints a table of the most important information about the specified deployments. You can filter the list using a label selector and the --selector flag.",
    parameters=ParametersSchema(
        type="object",
        properties={
            "namespace": {
                "type": "string",
                "description": "The namespace to get deployments from.",
            },
            "all_namespaces": {
                "type": "boolean",
                "description": "If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.",
                "default": False
            },
            "allow_missing_template_keys": {
                "type": "boolean",
                "description": "If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.",
                "default": True
            },
            "chunk_size": {
                "type": "integer",
                "description": "Return large lists in chunks rather than all at once. Pass 0 to disable. This flag is beta.",
                "default": 500
            },
            "field_selector": {
                "type": "string",
                "description": "Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. key1=value1,key2=value2).",
                "default": ""
            },
            "filename": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Filename, directory, or URL to files identifying the resource to get from a server."
            },
            "ignore_not_found": {
                "type": "boolean",
                "description": "If the requested object does not exist the command will return exit code 0.",
                "default": False
            },
            "kustomize": {
                "type": "string",
                "description": "Process the kustomization directory. This flag can't be used together with filename or recursive.",
                "default": ""
            },
            "label_columns": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Accepts a comma separated list of labels that are going to be presented as columns. Names are case-sensitive."
            },
            "no_headers": {
                "type": "boolean",
                "description": "When using the default or custom-column output format, don't print headers.",
                "default": False
            },
            "output": {
                "type": "string",
                "description": "Output format. One of: json, yaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file, custom-columns, custom-columns-file, wide",
                "enum": [
                    "json",
                    "yaml",
                    "name",
                    "go-template",
                    "go-template-file",
                    "template",
                    "templatefile",
                    "jsonpath",
                    "jsonpath-as-json",
                    "jsonpath-file",
                    "custom-columns",
                    "custom-columns-file",
                    "wide"
                ],
                "default": ""
            },
            "output_watch_events": {
                "type": "boolean",
                "description": "Output watch event objects when --watch or --watch-only is used.",
                "default": False
            },
            "raw": {
                "type": "string",
                "description": "Raw URI to request from the server. Uses the transport specified by the kubeconfig file.",
                "default": ""
            },
            "recursive": {
                "type": "boolean",
                "description": "Process the directory used in filename recursively.",
                "default": False
            },
            "selector": {
                "type": "string",
                "description": "Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. key1=value1,key2=value2)",
                "default": ""
            },
            "server_print": {
                "type": "boolean",
                "description": "If true, have the server return the appropriate table output. Supports extension APIs and CRDs.",
                "default": True
            },
            "show_kind": {
                "type": "boolean",
                "description": "If true, list the resource type for the requested object(s).",
                "default": False
            },
            "show_labels": {
                "type": "boolean",
                "description": "When printing, show all labels as the last column.",
                "default": False
            },
            "show_managed_fields": {
                "type": "boolean",
                "description": "If true, keep the managedFields when printing objects in JSON or YAML format.",
                "default": False
            },
            "sort_by": {
                "type": "string",
                "description": "If non-empty, sort list types using this field specification. The field specification is expressed as a JSONPath expression.",
                "default": ""
            },
            "subresource": {
                "type": "string",
                "description": "If specified, gets the subresource of the requested object. Must be one of [status scale].",
                "enum": ["status", "scale"],
                "default": ""
            },
            "template": {
                "type": "string",
                "description": "Template string or path to template file to use when -o=go-template, -o=go-template-file.",
                "default": ""
            },
            "watch": {
                "type": "boolean",
                "description": "After listing/getting the requested object, watch for changes.",
                "default": False
            },
            "watch_only": {
                "type": "boolean",
                "description": "Watch for changes to the requested object(s), without listing/getting first.",
                "default": False
            },
            "api_group": {
                "type": "string",
                "description": "The API group for the deployment resource (e.g., 'apps/v1').",
                "default": "apps/v1"
            }
        },
        required=["namespace"]
    )
)