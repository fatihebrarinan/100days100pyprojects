from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta


data = DataManager()
search = FlightSearch()
notification = NotificationManager()

token = search.get_token()
if not token:
    print("Failed to get token")
else:
    print(f"Got token {token}")
sheet_data = data.get_data()

date_input = input("At what date you want to travel? (Write in format YYYY/MM/DD): ")
date_input = date_input.split("/")
department_date = datetime(int(date_input[0]),int(date_input[1]),int(date_input[2]))

stay_input = input("How many days do you want to stay?: ")
return_date = department_date + timedelta(days=int(stay_input))

for item in sheet_data:
    lowest = 0
    for flights in search.search_flight(target = item["iataCode"], max_price=item["lowestPrice"], token=token, department_date=department_date, return_date=return_date):
        if float(flights["price"]["grandTotal"]) > lowest:
            lowest = float(flights["price"]["grandTotal"])
    if lowest == 0:
        print(f"Couldn't find tickets to {item['city']} from Istanbul cheaper than {item['lowestPrice']}TL at department date: {department_date.strftime("%Y/%m/%d")} and return date: {return_date.strftime("%Y/%m/%d")}.")
    else:
        notification.send_message(f"{item['city']} tickets from Istanbul for just {lowest}TL at department date: {department_date.strftime("%Y/%m/%d")} and return date: {return_date.strftime("%Y/%m/%d")}!")
        print(f"{item['city']} tickets from Istanbul for just {lowest}TL at department date: {department_date.strftime("%Y/%m/%d")} and return date: {return_date.strftime("%Y/%m/%d")}!")
