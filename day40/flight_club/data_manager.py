import requests
from config import SHEETY_PRICES_ENDPOINT, SHEETY_USERS_ENDPOINT, SHEETY_TOKEN

headers = {"Authorization": SHEETY_TOKEN}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            payload = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=payload,
                headers=headers
            )
            print(response.text)

    def get_user_data(self):
        response = requests.get(SHEETY_USERS_ENDPOINT, headers=headers)
        self.user_data = response.json()["users"]
        return self.user_data

    def add_user(self, first_name, last_name, email):
        payload = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(SHEETY_USERS_ENDPOINT, json=payload, headers=headers)
        print(response.text)