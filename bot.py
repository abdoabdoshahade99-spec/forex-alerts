name: تنبيهات الأسواق المالية

on:
  schedule:
    - cron: '50 23 * * 0-4'
    - cron: '50 8 * * 1-5'
    - cron: '50 5 * * 1-5'
    - cron: '50 13 * * 1-5'
    - cron: '50 14 * * 1-5'
    - cron: '50 19 * * 1-5'
  workflow_dispatch:

jobs:

  open-japan:
    if: github.event.schedule == '50 23 * * 0-4'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | الأسواق الآسيوية\n\n⚡️ 10 دقائق على افتتاح بورصة طوكيو\n🇯🇵 راقب الين الياباني وزوج USDJPY\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"

  open-london:
    if: github.event.schedule == '50 8 * * 1-5'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | الأسواق الأوروبية\n\n⚡️ 10 دقائق على افتتاح بورصة لندن\n🇬🇧 راقب الجنيه الإسترليني وزوج GBPUSD\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"

  close-japan:
    if: github.event.schedule == '50 5 * * 1-5'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | إغلاق الأسواق الآسيوية\n\n⚡️ 10 دقائق على إغلاق بورصة طوكيو\n🇯🇵 أغلق صفقاتك على الين والأسواق الآسيوية\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"

  open-usa:
    if: github.event.schedule == '50 13 * * 1-5'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | الأسواق الأمريكية\n\n⚡️ 10 دقائق على افتتاح وول ستريت\n🗽 تأهب للتداول وراقب فرص الدخول\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"

  close-london:
    if: github.event.schedule == '50 14 * * 1-5'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | إغلاق الأسواق الأوروبية\n\n⚡️ 10 دقائق على إغلاق بورصة لندن\n🇬🇧 أغلق صفقاتك على الجنيه والأسواق الأوروبية\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"

  close-usa:
    if: github.event.schedule == '50 19 * * 1-5'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python bot.py
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          MESSAGE: "🔔 تنبيه | إغلاق الأسواق الأمريكية\n\n⚡️ 10 دقائق على إغلاق وول ستريت\n📉 أغلق صفقاتك وراجع نتائج اليوم\n\n📌 للتحليلات والإشارات المباشرة:\n🔐 القناة الخاصة: https://t.me/abdoshahade1\n📢 القناة العامة: https://t.me/inv7mindforex"
