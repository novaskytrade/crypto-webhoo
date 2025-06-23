from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received:", data)
    return jsonify({"status": "success", "message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
    import requests

TELEGRAM_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsD-Kd9LKJjV1FdSshqU"
TELEGRAM_CHAT_ID = "6110698820"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    print("Response status:", response.status_code)
    print("Response body:", response.text)

# 🔁 Run this once when the server starts
if __name__ == "__main__":
    send_telegram_message("✅ Telegram bot test message successful!")
