import requests
import datetime
from requests.auth import HTTPBasicAuth
import os

basic = HTTPBasicAuth(os.environ["SHEETY_USERNAME"], os.environ["PASSWORD"])

headers = {
    "x-app-id":os.environ["APP_ID"],
    "x-app-key":os.environ["APP_KEY"],
}
workout_parameters = {
    "query":input("Write your exercises: "),
    "weight_kg":80,
    "height_cm":180,
    "age":19,
}


workout_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=workout_parameters, headers=headers)
workout_response.raise_for_status()

workout_data = workout_response.json()
exercise_type = workout_data["exercises"][0]["user_input"]
exercise_duration = workout_data["exercises"][0]["duration_min"]
exercise_calories = workout_data["exercises"][0]["nf_calories"]


today = datetime.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_hour = today.strftime("%H:%M:%S")


sheety_parameters = {
    "workout":{
        "date":today_date,
        "time":today_hour,
        "exercise":exercise_type.title(),
        "duration":exercise_duration,
        "calories":exercise_calories
    }
}

sheety_response = requests.post(os.environ["SHEET_ENDPOINT"], json=sheety_parameters, auth=basic)
sheety_response.raise_for_status()