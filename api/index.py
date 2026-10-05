import os
import requests
from http.server import BaseHTTPRequestHandler

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID = "-1004308649953"
REMINDER_TOPIC_ID = 42


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = """📋 Daily Report Reminder

Good evening everyone!

Please don't forget your daily report for today.

Thank you! ☺️
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHAT_ID,
            "message_thread_id": REMINDER_TOPIC_ID,
            "text": message
        }

        response = requests.post(
            url,
            data=data,
            timeout=10
        )

        if response.ok:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Reminder sent successfully!")
        else:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Failed to send reminder")