import json
from sprint_2.lesson_2_1_web_search import web_search
from sprint_2.lesson_2_2_file_io import write_file


def read_file(file_path: str) -> str:
    import os
    resolved = os.path.abspath(file_path)
    OUTPUT_DIR = os.path.abspath("output")

    if not resolved.startswith(OUTPUT_DIR + os.sep) and resolved != OUTPUT_DIR:
        raise ValueError(f"Security violation: reading outside output/ is not allowed")

    with open(resolved, "r", encoding="utf-8") as f:
        return f.read()


TOOL_ROUTER = {
    "web_search": lambda args: web_search(**args),
    "read_file": lambda args: read_file(**args),
    "write_file": lambda args: write_file(**args),
}


def execute_tool_calls(message_obj: dict) -> list:
    results = []

    for tool_call in message_obj.get("tool_calls", []):
        func = tool_call.get("function", {})
        name = func.get("name")
        arguments = json.loads(func.get("arguments", "{}"))

        handler = TOOL_ROUTER.get(name)
        if handler is None:
            raise ValueError(f"Unknown tool: {name}")

        output = handler(arguments)

        results.append({
            "role": "tool",
            "tool_call_id": tool_call["id"],
            "content": str(output)
        })

    return results
