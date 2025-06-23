import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsDKd9LKJjV1FdSshqU"
CHAT_ID = "6110698820"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)

@app.route("/")
def home():
    return "✅ Crypto TrendBot is live", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "🚨 Alert Triggered (No message provided)")
    send_message(message)
    return {"status": "sent"}, 200

if __name__ == "__main__":
    send_message("🚀 Success! Bot is deployed and listening for alerts.")
    app.run(host="0.0.0.0", port=10000)
