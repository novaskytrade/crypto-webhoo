import requests
import pandas as pd

SYMBOL = "BTCUSDT"
INTERVAL = "15m"
LIMIT = 100

# Your Telegram bot credentials
TELEGRAM_BOT_TOKEN = "7748226811:AAFZB0KqLsQCtqW5AsDKd9LKJjV1FdSshqU"
TELEGRAM_CHAT_ID = "6110698820"

def fetch_binance_klines(symbol, interval, limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])
    df["close"] = df["close"].astype(float)
    return df

def calculate_ema_trend(df):
    df["EMA20"] = df["close"].ewm(span=20).mean()
    df["EMA50"] = df["close"].ewm(span=50).mean()
    latest = df.iloc[-1]
    if latest["EMA20"] > latest["EMA50"]:
        return "Bullish Trend ✅"
    elif latest["EMA20"] < latest["EMA50"]:
        return "Bearish Trend ❌"
    else:
        return "Choppy/Neutral ⚠️"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    df = fetch_binance_klines(SYMBOL, INTERVAL, LIMIT)
    trend = calculate_ema_trend(df)
    if "Trend" in trend:
        send_telegram_message(f"📈 {SYMBOL} 15m Trend Update: {trend}")   
