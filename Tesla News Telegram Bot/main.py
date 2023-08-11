import requests
import os
from dotenv import load_dotenv
from telegram_sender import send_telegram_msg
import math

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

############################Stock difference calculation of last two days############################
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
last_two_dates = list(stock_data.items())[:2]
last_day_close = float(last_two_dates[0][1]["4. close"])
previous_day_close = float(last_two_dates[1][1]["4. close"])
difference = last_day_close - previous_day_close
percentage = ((difference/previous_day_close)*100)

# move symbol
move = ""
if percentage <= -5:
    move = "🔻"
elif percentage >= 5:
    move = "🔺"

############################Get News############################
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

def get_news():
    message = f"TSLA:{move}{math.floor(percentage)}%\n"
    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()
    articles = response.json()["articles"][:3]
    for article in articles:
        title = article["title"]
        brief = article["description"]
        message += f'''
Title: {title}
Brief: {brief}
'''
    return message

# if there's a variation of -5/5 in the stock send message with the first three news

if percentage <= -5 or percentage >= 5:
    message = get_news()
    send_telegram_msg(message)
