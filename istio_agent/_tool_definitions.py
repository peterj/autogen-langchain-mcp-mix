from autogen_core.tools import ParametersSchema, ToolSchema



TOOL_VERIFY_INSTALL = ToolSchema(
    name="verify_install",
    description="Verifies Istio installation on the current Kubernetes cluster.",
)


# TOOL_PAGE_DOWN = ToolSchema(
#     name="page_down",
#     description="Scroll the viewport DOWN one page-length in the current file and return the new viewport content.",
# )


# TOOL_FIND_ON_PAGE_CTRL_F = ToolSchema(
#     name="find_on_page_ctrl_f",
#     description="Scroll the viewport to the first occurrence of the search string. This is equivalent to Ctrl+F.",
#     parameters=ParametersSchema(
#         type="object",
#         properties={
#             "search_string": {
#                 "type": "string",
#                 "description": "The string to search for on the page. This search string supports wildcards like '*'",
#             },
#         },
#         required=["search_string"],
#     ),
# )


# TOOL_FIND_NEXT = ToolSchema(
#     name="find_next",
#     description="Scroll the viewport to next occurrence of the search string.",
# )