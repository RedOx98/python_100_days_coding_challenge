from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LOS"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification = NotificationManager()

for destination in sheet_data:
    flight = flight_search.get_flight_data(ORIGIN_CITY_IATA, destination["iataCode"])
    if flight:
        price = float(flight["price"]["total"])
        if price < destination["lowestPrice"]:
            message = f"Low price alert! ✈️ Only ${price} to fly from {ORIGIN_CITY_IATA} to {destination['city']}."
            notification.send_sms(message)