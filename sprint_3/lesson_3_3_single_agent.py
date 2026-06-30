import os
import json
import urllib.request
from dotenv import load_dotenv
from sprint_3.lesson_3_1_schemas import TOOLS
from sprint_3.lesson_3_2_tool_parsing import execute_tool_calls

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = []

print("Single-Agent Loop (type 'exit' or 'quit' to stop)")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    for iteration in range(5):
        payload = {
            "model": "poolside/laguna-m.1:free",
            "messages": messages,
            "tools": TOOLS
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(API_URL, data=data, headers=headers)

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))

        message = result["choices"][0]["message"]
        messages.append(message)

        if message.get("content"):
            print(f"\nAssistant: {message['content']}")
            break

        if message.get("tool_calls"):
            tool_results = execute_tool_calls(message)
            messages.extend(tool_results)
