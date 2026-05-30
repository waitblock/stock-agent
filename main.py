import os
import requests
import json
import parse
import send

api_key = os.environ["OPENROUTER_API_KEY"]
sender = os.environ["SENDER_EMAIL"]
app_pw = os.environ["GOOGLE_APP_PASSWORD"]
receiver = os.environ["RECEIVER_EMAIL"]

with open("prompt.txt") as prompt_file:
	prompt = prompt_file.read()

def main():
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
				"content": prompt
			}
			],
			"tools": [
				{"type": "openrouter:web_search"}
			]
		},
		timeout=120
	)

	data = response.json()
	print(data)

	print("Generating response HTML...")
	response_html = parse.generate_html(data)

	print("Sending email...")
	send.send_email(response_html, sender, app_pw, receiver)

if __name__ == "__main__":
	main()
