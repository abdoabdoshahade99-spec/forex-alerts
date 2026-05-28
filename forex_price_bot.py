import os
import sys
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID   = os.environ["CHAT_ID"]

SYMBOLS = {
    "GC=F":  ("🥇", "الذهب     XAUUSD"),
    "EURUSD=X": ("💶", "يورو دولار EURUSD"),
    "GBPUSD=X": ("💷", "جنيه دولار GBPUSD"),
    "CL=F":  ("🛢️", "النفط الخام  WTI"),
    "DX-Y.NYB": ("💵", "مؤشر الدولار DXY"),
}

def get_price(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    data = resp.json()
    price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    prev  = data["chart"]["result"][0]["meta"]["chartPreviousClose"]
    change = ((price - prev) / prev) * 100
    return price, change

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
    now = datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M — %d/%m/%Y")
    lines = []

    for symbol, (icon, name) in SYMBOLS.items():
        try:
            price, change = get_price(symbol)
            arrow = "🟢 ▲" if change >= 0 else "🔴 ▼"
            if symbol in ["EURUSD=X", "GBPUSD=X"]:
                formatted = f"{price:.5f}"
            elif symbol == "DX-Y.NYB":
                formatted = f"{price:.3f}"
            else:
                formatted = f"${price:,.2f}"
            lines.append(f"{icon} {name}: {formatted}  {arrow} {abs(change):.2f}%")
        except Exception as e:
            print(f"خطا في {symbol}: {e}")

    prices_text = "\n".join(lines)

    message = (
        f"📊 اسعار الاسواق المباشرة\n"
        f"━━━━━━━━━━━━━━━━\n\n"
        f"{prices_text}\n\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"🕐 اخر تحديث: {now}\n\n"
        f"📌 للتحليلات والاشارات المباشرة:\n"
        f"🔐 القناة الخاصة: https://t.me/abdoshahade1\n"
        f"📢 القناة العامة: https://t.me/inv7mindforex\n"
        f"🔗 دخول القناة الخاصة: https://t.me/inv7mindforex/13964"
    )

    send_message(message)
