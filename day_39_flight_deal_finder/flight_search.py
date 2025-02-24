import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:

    def get_token(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        # Amadeus API credentials and token endpoint
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret,
        }
        token_response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=data)
        token_response.raise_for_status()
        token_data = token_response.json()
        access_token = token_data['access_token']
        return access_token


    def search_flight(self,target,max_price,token, department_date,return_date):

        search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"


        search_parameters = {
            "originLocationCode":"SAW",
            "destinationLocationCode":target,
            "departureDate":department_date.strftime("%Y-%m-%d"),
            "returnDate":return_date.strftime("%Y-%m-%d"),
            "adults":1,
            "travelClass":"ECONOMY",
            "currencyCode":"TRY",
            "maxPrice":max_price,
            #"nonStop":"true",
        }
        search_header = {
            "Authorization": f"Bearer {token.strip()}"
        }

        search_response = requests.get(url=search_endpoint, params=search_parameters, headers=search_header)
        if search_response.status_code == 401:
            print(f"Unauthorized request: {search_response.json()}")
        search_response.raise_for_status()
        search_data = search_response.json()
        return search_data["data"]
