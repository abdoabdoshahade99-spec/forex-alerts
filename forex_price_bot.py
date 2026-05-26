import os
import sys
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID   = os.environ["CHAT_ID"]

def get_prices():
    # مفتاح API مجاني من twelvedata.com
    API_KEY = os.environ["TWELVE_API_KEY"]
    
    symbols = "XAU/USD,EUR/USD,GBP/USD,WTI/USD,DXY"
    url = f"https://api.twelvedata.com/price?symbol={symbols}&apikey={API_KEY}"
    
    resp = requests.get(url, timeout=10)
    data = resp.json()
    return data

def format_change(price, symbol):
    # رموز بصرية لكل أداة
    icons = {
        "XAU/USD": "🥇",
        "EUR/USD": "💶",
        "GBP/USD": "💷",
        "WTI/USD": "🛢️",
        "DXY":     "💵"
    }
    names = {
        "XAU/USD": "الذهب    XAUUSD",
        "EUR/USD": "يورو دولار EURUSD",
        "GBP/USD": "جنيه دولار GBPUSD",
        "WTI/USD": "النفط الخام WTI",
        "DXY":     "مؤشر الدولار DXY"
    }
    icon = icons.get(symbol, "📊")
    name = names.get(symbol, symbol)
    return f"{icon} {name}: {price}"

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
    data = get_prices()

    now = datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M — %d/%m/%Y")

    symbols = ["XAU/USD", "EUR/USD", "GBP/USD", "WTI/USD", "DXY"]
    
    lines = []
    for symbol in symbols:
        if symbol in data and "price" in data[symbol]:
            price = float(data[symbol]["price"])
            # تنسيق الأرقام حسب الأداة
            if symbol == "XAU/USD":
                formatted = f"${price:,.2f}"
            elif symbol in ["EUR/USD", "GBP/USD"]:
                formatted = f"{price:.5f}"
            elif symbol == "WTI/USD":
                formatted = f"${price:,.2f}"
            else:  # DXY
                formatted = f"{price:.3f}"
            lines.append(format_change(formatted, symbol))

    prices_text = "\n".join(lines)

    message = (
        f"📊 اسعار الاسواق المباشرة\n\n"
        f"{prices_text}\n\n"
        f"🕐 اخر تحديث: {now}\n\n"
        f"📌 للتحليلات والاشارات المباشرة:\n"
        f"🔐 القناة الخاصة: https://t.me/abdoshahade1\n"
        f"📢 القناة العامة: https://t.me/inv7mindforex\n"
        f"🔗 دخول القناة الخاصة: https://t.me/inv7mindforex/13964"
    )

    send_message(message)
