import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID = "-1004308649953"
REMINDER_TOPIC_ID = 42

message = """📋 Daily Report Reminder

Good evening everyone!

Please don't forget to submit your daily report for today.

Thank you! ☺️
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "message_thread_id": REMINDER_TOPIC_ID,
    "text": message
}

response = requests.post(url, data=data, timeout=10)

if response.ok:
    print("✅ Reminder sent to Reminder topic!")
else:
    print("❌ Failed:", response.text)