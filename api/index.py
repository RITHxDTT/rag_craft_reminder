import os
import requests
from http.server import BaseHTTPRequestHandler

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CRON_SECRET = os.getenv("CRON_SECRET")

CHAT_ID = "-1004308649953"
REMINDER_TOPIC_ID = 42


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        # Only allow Vercel Cron to call this endpoint
        authorization = self.headers.get("Authorization")

        if authorization != f"Bearer {CRON_SECRET}":
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"Unauthorized")
            return

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

        try:
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

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())