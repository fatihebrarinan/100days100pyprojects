import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def send_message(self,message):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        msg = client.messages.create(
            from_=os.getenv("TWILIO_NUM"),
            body=message,
            to=os.getenv("MY_NUM")
        )