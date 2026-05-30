import json
import markdown

def generate_html(data):
	content = data["choices"][0]["message"]["content"]
	html = markdown.markdown(content, extensions=["tables", "fenced_code", "codehilite", "toc"])

	html_page = f"""<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Markdown Render</title>
		<style>
		    body {{
		    	font-size: 18px;
		        font-family: Arial, sans-serif;
		        max-width: 900px;
		        margin: 40px auto;
		        padding: 20px;
		        line-height: 1.6;
		        background-color: #f5f5f5;
		        color: #333;
		    }}

		    .container {{
		        background: white;
		        padding: 40px;
		        border-radius: 10px;
		        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
		    }}

		    h1, h2, h3 {{
		        color: #222;
		    }}

		    code {{
		        background: #eee;
		        padding: 2px 6px;
		        border-radius: 4px;
		        font-family: monospace;
		    }}

		    pre {{
		        background: #272822;
		        color: #f8f8f2;
		        padding: 16px;
		        border-radius: 8px;
		        overflow-x: auto;
		    }}

		    pre code {{
		        background: transparent;
		        padding: 0;
		        color: inherit;
		    }}

		    table {{
		        border-collapse: collapse;
		        width: 100%;
		        margin-top: 20px;
		    }}

		    th, td {{
		        border: 1px solid #ccc;
		        padding: 12px;
		        text-align: left;
		    }}

		    th {{
		        background-color: #f0f0f0;
		    }}

		    tr:nth-child(even) {{
		        background-color: #fafafa;
		    }}

		    blockquote {{
		        border-left: 4px solid #ccc;
		        padding-left: 16px;
		        color: #666;
		        margin-left: 0;
		    }}

		    a {{
		        color: #0366d6;
		        text-decoration: none;
		    }}

		    a:hover {{
		        text-decoration: underline;
		    }}
		</style>
	</head> <body> <div class="container"> {html} </div> </body> </html> """

	return html_page