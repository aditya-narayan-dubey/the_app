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

messages = [
    {"role": "system", "content": "You are a knowledgeable, precise assistant. Answer questions clearly and concisely. When you do not know something, say so rather than making up information."}
]

print("Interactive Chat (type 'exit' or 'quit' to stop)")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "poolside/laguna-m.1:free",
        "messages": messages
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, headers=headers)

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

    response_text = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": response_text})

    print(f"\nAssistant: {response_text}")
