import smtplib
from email.message import EmailMessage
from datetime import date

def send_email(content, sender, pw, receiver, fallback="Your email client does not support HTML."):
	msg = EmailMessage()
	msg["Subject"] = f"Stock Report {date.today()}"
	msg["From"] = sender
	msg["To"] = receiver

	msg.set_content(fallback)
	msg.add_alternative(content, subtype="html")

	with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
	    smtp.login(sender, pw)
	    smtp.send_message(msg)
