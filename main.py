import os
from dotenv import load_dotenv
import requests
import json
import parse
import send

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
sender = os.getenv("SENDER_EMAIL")
app_pw = os.getenv("GOOGLE_APP_PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")

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
				"content": "You are an expert advising a person about stocks that is good at being concise. What are the biggest stocks to watch in the upcoming days? Explain why each stock is a good buy in simple terms. Include a disclaimer that you are not giving financial advice."
			}
			],
			"tools": [
				{"type": "openrouter:web_search"}
			]
		}
	)

	data = response.json()

	print("Generating response HTML...")
	response_html = parse.generate_html(data)

	print("Writing to log...")
	with open("response.log", "w") as fout:
		json.dump(data, fout)

	print("Sending email...")
	send.send_email(response_html, sender, app_pw, receiver)

if __name__ == "__main__":
	main()
