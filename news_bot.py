import os
import sys
import json
import hashlib
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN    = os.environ["BOT_TOKEN"]
CHAT_ID      = os.environ["CHAT_ID"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]

# ==============================
# ترجمة مجانية بدون API key
# ==============================
def translate_to_arabic(text):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "en",
            "tl": "ar",
            "dt": "t",
            "q": text
        }
        resp = requests.get(url, params=params, timeout=10)
        result = resp.json()
        translated = ""
        for item in result[0]:
            if item[0]:
                translated += item[0]
        return translated
    except Exception as e:
        print(f"خطا في الترجمة: {e}")
        return text

# ==============================
# جلب الأخبار الهامة
# ==============================
def get_forex_news():
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWS_API_KEY,
        "q": "forex OR gold OR XAUUSD OR interest rate OR fed OR dollar OR EUR/USD OR GBP/USD",
        "language": "en",
        "category": "business",
        "size": 5
    }
    resp = requests.get(url, params=params, timeout=10)
    data = resp.json()
    return data.get("results", [])

# ==============================
# تتبع الأخبار المنشورة
# ==============================
def get_posted_ids():
    try:
        with open("posted_news.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_posted_ids(ids):
    ids = ids[-50:]
    with open("posted_news.json", "w") as f:
        json.dump(ids, f)

def news_id(article):
    return hashlib.md5(article.get("title", "").encode()).hexdigest()

# ==============================
# إرسال الرسالة
# ==============================
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": False
    }
    resp = requests.post(url, json=payload, timeout=10)
    result = resp.json()
    if result.get("ok"):
        print("تم الارسال بنجاح!")
    else:
        print(f"خطا: {result}")

# ==============================
# التشغيل الرئيسي
# ==============================
if __name__ == "__main__":
    print("جلب الاخبار...")
    articles = get_forex_news()
    posted_ids = get_posted_ids()
    new_ids = list(posted_ids)
    sent_count = 0

    for article in articles:
        aid = news_id(article)

        if aid in posted_ids:
            print(f"خبر مكرر: {article.get('title', '')[:50]}")
            continue

        title       = article.get("title", "")
        description = article.get("description", "") or article.get("content", "") or ""
        link        = article.get("link", "")

        print(f"ترجمة: {title[:50]}...")

        title_ar = translate_to_arabic(title)
        desc_ar  = translate_to_arabic(description[:300]) if description else ""

        now = datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M — %d/%m/%Y")

        message = (
            f"📰 خبر عاجل | فوركس وذهب\n\n"
            f"🔹 {title_ar}\n\n"
            f"{desc_ar}\n\n"
            f"🔗 المصدر: {link}\n\n"
            f"🕐 {now}\n\n"
            f"📌 للتحليلات والاشارات:\n"
            f"🔐 القناة الخاصة: https://t.me/abdoshahade1\n"
            f"📢 القناة العامة: https://t.me/inv7mindforex"
        )

        send_message(message)
        new_ids.append(aid)
        sent_count += 1

    save_posted_ids(new_ids)
    print(f"تم نشر {sent_count} خبر جديد")
