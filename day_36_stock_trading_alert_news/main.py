import requests
import math
from twilio.rest import Client

STOCK = "Stock"
stock_api_key = "[]"
news_api_key = "[]"


stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key,
}
connection = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
connection.raise_for_status()
data = connection.json()
time_series = data["Time Series (Daily)"]
yesterday_day = list(time_series)[0]
previous_day = list(time_series)[1]
yesterday_data = float(time_series[yesterday_day]["4. close"])
previous_data = float(time_series[previous_day]["4. close"])

if math.fabs(yesterday_data - previous_data) > previous_data*(1/20):

    news_parameters = {
        "q": "tesla",
        "from": "2025-01-01",
        "sortBy": "publishedAt",
        "apiKey": news_api_key,
    }
    response = requests.get("https://newsapi.org/v2/top-headlines", params=news_parameters)
    news_data = response.json()
    new_title = news_data["articles"][0]["title"]
    print(new_title)
    new_description = news_data["articles"][0]["description"]
    print(new_description)


    percent_change = round((yesterday_data-previous_data)/previous_data * 100, 2)
    print(percent_change)

    account_sid = '[]'
    auth_token = '[]'
    client = Client(account_sid, auth_token)

    body = f"{percent_change}% change on Tesla.\n{new_title}\n{new_description}"

    message = client.messages.create(
        from_='[num]',
        body=body,
        to='[num]'
    )

    print(message.status)
    # For some unknown reasons, when i add the news to the message, the SMS doesn't send now.


