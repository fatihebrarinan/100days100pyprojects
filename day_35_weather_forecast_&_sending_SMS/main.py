import requests
from twilio.rest import Client

account_sid = 'sample_sid'
auth_token = 'sample_token'

api_key = "sample_key"
parameters = {
    "lat":0,
    "lon":0,
    "appid":api_key,
    "cnt":4,
}
connection = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
connection.raise_for_status()
weather_data = connection.json()

umbrella_needed = False
for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        umbrella_needed = True
if umbrella_needed:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='sample_num',
        to='sample_num',
        body="hi",
    )
    print(message.status)