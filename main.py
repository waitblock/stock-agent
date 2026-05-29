import os
from dotenv import load_dotenv
import requests
import json
import parse

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

print("Sending request to OpenRouter...")
response = requests.post(
  "https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
  },
  json={
    "model": "openai/gpt-oss-120b:free",
    "messages": [
      {
        "role": "user",
        "content": "You are an expert advising a person about stocks that is good at being concise. What are the biggest stocks to watch next week? Explain why each stock is a good buy."
      }
    ],
    "tools": [
      {"type": "openrouter:web_search"}
    ]
  }
)

data = response.json()

print("Generating response HTML...")
parse.generate_html(data)

print("Writing to log...")
with open("response.log", "w") as fout:
	json.dump(data, fout)
