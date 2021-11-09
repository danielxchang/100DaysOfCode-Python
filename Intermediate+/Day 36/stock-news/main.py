import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TRIGGER = 4

AV_API = os.environ.get("ALPHA_VANTAGE_API")
AV_ENDPOINT = 'https://www.alphavantage.co/query'
av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API
}

NEWS_API = os.environ.get("NEWS_API")
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

account_sid = 'AC57a33e32f8abccc7ecee66067a26a29f'
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
phone_number = os.environ.get("PHONE_NUMBER")


def get_news():
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    first_three_articles = news_response.json()['articles'][:3]
    return [{'title': article['title'], 'description': article['description']} for article in first_three_articles]


def stock_news():
    # Retrieve daily stock price data from Alpha Vantage
    response = requests.get(url=AV_ENDPOINT, params=av_params)
    response.raise_for_status()
    stock_data = response.json()
    daily_data = stock_data['Time Series (Daily)']
    daily_list = [float(data['4. close']) for date, data in daily_data.items()]

    # Calculate price change between last two trading days
    last_close, day_before_close = daily_list[:2]
    price_change = round((last_close - day_before_close) / day_before_close * 100, 2)

    # send text messages of three articles if price change greater than TRIGGER
    if abs(price_change) >= TRIGGER:
        articles = get_news()
        client = Client(account_sid, auth_token)
        for article in articles:
            message = client.messages.create(
                messaging_service_sid='MGdbdbce2db415f5108c04c169fd828d27',
                body=f"{STOCK}: {'🔺' if price_change > 0 else '🔻'}{abs(price_change)}%\n\n"
                     f"Headline: {article['title']}\n\n"
                     f"Brief: {article['description']}",
                to=phone_number
            )
            print(message.status)


if __name__ == "__main__":
    stock_news()
