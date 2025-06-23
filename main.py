import requests

BOT_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsD-Kd9LKJjV1FdSshqU"
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

# Trigger message
if __name__ == "__main__":
    send_message("🚀 Success! Your bot can now send messages.") 
    import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsD-Kd9LKJjV1FdSshqU"
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
    send_message("🚀 Bot is now live and ready!")
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
