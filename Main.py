import requests

TELEGRAM_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsDKd9LKJjV1FdSshqU"
TELEGRAM_CHAT_ID = "6110698820"  # Your chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("❌ Telegram send error:", e)

if __name__ == "__main__":
    send_telegram_message("✅ Telegram is connected to your crypto webhook!"
  if __name__ == "__main__":
    send_telegram_message("✅ Telegram is connected to your crypto webhook!")                      )
