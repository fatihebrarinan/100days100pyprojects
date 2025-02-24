import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
        self.SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
    def get_data(self):
        basic = HTTPBasicAuth(self.SHEETY_USERNAME,self.SHEETY_PASSWORD)

        sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

        response = requests.get(url=sheety_endpoint, auth=basic)
        return response.json()["prices"]