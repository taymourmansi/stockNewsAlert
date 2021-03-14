import requests
import pandas
import datetime
import os
from twilio.rest import Client
from math import fabs
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
SENDER_NUMBER = "Twilio Phone Number Here"
RECEIVER_NUMBER = "Your Phone Number Here"

stockKey = os.environ.get("STOCK_API_KEY")
newsKey = os.environ.get("NEWS_API_KEY")

accountSid = os.environ.get("TWILIO_ACCOUNT_SID")
authToken = os.environ.get("TWILIO_AUTH_TOKEN")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stockParameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":stockKey,
}
newsParameteres={
    "q": COMPANY_NAME,
    "apikey":newsKey,
}

today = datetime.datetime.today().date()
yesterday = (today - datetime.timedelta(1))
beforeYesterday = (today - datetime.timedelta(2))

stockResponse = requests.get(url=STOCK_ENDPOINT,params=stockParameters)
stockData = stockResponse.json()
stockYesterday = stockData["Time Series (Daily)"][str(yesterday)]["4. close"]
stockBYesterday = stockData["Time Series (Daily)"][str(beforeYesterday)]["4. close"]

difference = round((1-(float(stockYesterday) / float(stockBYesterday))),5)
if difference >= 0.05:
    symbol = "🔺"
elif difference <= 0.05:
    symbol = "🔻"
if abs(difference) >= 0.05:
    newsResponse = requests.get(url=NEWS_ENDPOINT,params=newsParameteres)
    newsData = newsResponse.json()

    newsArticles = newsData["articles"][:3]
    for article in newsArticles:
        client = Client(accountSid, authToken)
        message = client.messages \
            .create(
            body=f"TSLA: {symbol}{abs(difference *100)}% \nAuthor: {article['author']}\nDescription: {article['description']}\nURL: {article['url']}",
            from_=SENDER_NUMBER,
            to=RECEIVER_NUMBER
        )



