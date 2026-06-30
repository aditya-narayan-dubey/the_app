import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Interactive Chat (type 'exit' or 'quit' to stop)")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    payload = {
        "model": "poolside/laguna-m.1:free",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, headers=headers)

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

    print(f"\nAssistant: {result['choices'][0]['message']['content']}")
