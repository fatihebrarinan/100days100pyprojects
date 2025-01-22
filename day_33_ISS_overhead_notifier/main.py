import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 0
MY_LNG = 0

email = "ap9872355@gmail.com"
password = "sample_password"
connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)


def within_range():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if (MY_LAT + 5 > iss_lat > MY_LAT - 5) and (MY_LNG + 5 > iss_lng > MY_LNG - 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": "Europe/Istanbul"
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if sunrise <= hour_now <= sunset:
        return False
    else:
        return True


while True:
    time.sleep(60)
    if within_range() and is_night():
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Look up! ISS is there!\n\nISS is roaming through the night sky above you."
        )
