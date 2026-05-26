import os
import sys
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID   = os.environ["CHAT_ID"]
MESSAGE   = os.environ["MESSAGE"]

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": True
    }
    resp = requests.post(url, json=payload, timeout=10)
    result = resp.json()
    if result.get("ok"):
        print("تم الارسال بنجاح!")
    else:
        print(f"خطا: {result}")
        sys.exit(1)

if __name__ == "__main__":
    send_message(MESSAGE)
