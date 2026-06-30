import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_URL = "https://api.tavily.com/search"


def web_search(query: str, max_results: int = 3) -> str:
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": max_results
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TAVILY_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

    parts = []
    for item in result.get("results", []):
        parts.append(f"Title: {item['title']}\nURL: {item['url']}\nSummary: {item['content']}\n")

    return "\n---\n".join(parts)


if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else input("Search query: ")
    print(web_search(query))
