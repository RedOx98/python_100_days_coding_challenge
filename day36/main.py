import requests
from twilio.rest import Client
from datetime import datetime

# ---------------------------- CONFIG ---------------------------- #
STOCK = "TSLA"  # You can change this
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

TWILIO_PHONE = "+1234567890"
MY_PHONE = "+234XXXXXXXXXX"

# ---------------------------- STEP 1: STOCK DATA ---------------------------- #
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_close = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_close = float(day_before_yesterday_data["4. close"])

# Calculate percentage difference
difference = abs(yesterday_close - day_before_close)
diff_percent = (difference / yesterday_close) * 100

up_down = "🔺" if yesterday_close > day_before_close else "🔻"

print(f"{COMPANY_NAME} change: {diff_percent:.2f}% {up_down}")

# ---------------------------- STEP 2: TRIGGER NEWS ---------------------------- #
if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK}: {up_down}{diff_percent:.2f}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]

    # ---------------------------- STEP 3: SEND ALERT ---------------------------- #
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(f"✅ Sent message SID: {message.sid}")
else:
    print("No significant movement today.")
