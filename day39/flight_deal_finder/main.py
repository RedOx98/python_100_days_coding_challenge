import requests
from datetime import datetime
from amadeus import Client, ResponseError
from datetime import datetime, timedelta
from twilio.rest import Client as TwilioClient

# ------------------- CONFIG ------------------- #
AMADEUS_CLIENT_ID = "XXXXXXXXX"
AMADEUS_CLIENT_SECRET = "XXXXX"

# ✅ Initialize Amadeus client
amadeus = Client(
    client_id=AMADEUS_CLIENT_ID,
    client_secret=AMADEUS_CLIENT_SECRET
)

ORIGIN_IATA           = "LOS"      # Change as needed
MAX_STOP_OVERS        = 0          # Non-stop flights only (optional)

# ---------------- SHEETY CONFIG ---------------- #
SHEETY_ENDPOINT = "https://api.sheety.co/cfe410972db5adc5401fb03798265f66/flightDeals/sheet1"
SHEETY_TOKEN = "Bearer bkcajivzkSNmvl.bzchvcxzfjxbjkJHZc"

headers_sheety = {
    "Authorization": SHEETY_TOKEN
}

sample_data = [
    {"city": "London", "iataCode": "LHR", "targetPrice": 500},
    {"city": "New York", "iataCode": "JFK", "targetPrice": 800},
    {"city": "Paris", "iataCode": "CDG", "targetPrice": 550},
    {"city": "Lagos", "iataCode": "LOS", "targetPrice": 700},
]

# ---------------- WRITE DATA ---------------- #
def add_sample_data():
    today = datetime.now().strftime("%Y-%m-%d")
    for entry in sample_data:
        payload = {
            "sheet1": {
                "city": entry["city"],
                "iataCode": entry["iataCode"],
                "targetPrice": entry["targetPrice"],
                "dateAdded": today
            }
        }
        response = requests.post(SHEETY_ENDPOINT, json=payload, headers=headers_sheety)
        print("Added:", response.text)


# ---------------- HELPER FUNCTIONS ---------------- #
def get_destinations():
    """Read destination list (city, iata, target) from Google Sheet."""
    response = requests.get(SHEETY_ENDPOINT, headers=headers_sheety)
    response.raise_for_status()
    data = response.json().get("sheet1", [])
    return data


def search_flight(dest_iata, target_price):
    """Query Amadeus for flight offers and check if price falls below target."""
    depart_date = (datetime.now() + timedelta(days=7)).date().isoformat()
    return_date = (datetime.now() + timedelta(days=30)).date().isoformat()
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode      = ORIGIN_IATA,
            destinationLocationCode = dest_iata,
            departureDate           = depart_date,
            returnDate              = return_date,
            adults                  = 1,
            nonStop                 = True,
            currencyCode            = "USD"
        )
        offers = response.data
        print(offers)
        if not offers:
            return None

        cheapest = offers[0]
        price    = float(cheapest["price"]["total"])
        if price <= target_price:
            return {
                "price": price,
                "dest":  dest_iata,
                "departDate": depart_date,
                "returnDate": return_date,
                "offer": cheapest
            }
        return None

    except ResponseError as e:
        print("Amadeus API error:", e)
        return None


def send_alert(deal):
    """Send SMS notification via Twilio about the deal."""
    message = (f"Flight Deal Alert! ✈️ {ORIGIN_IATA} → {deal['dest']} at ${deal['price']}\n"
               f"Depart: {deal['departDate']}, Return: {deal['returnDate']}")
    msg = twilio.messages.create(body=message, from_=TWILIO_FROM, to=MY_PHONE)
    print("Alert sent. SID:", msg.sid)


# ---------------- MAIN FLOW ---------------- #
if __name__ == "__main__":
    destinations = get_destinations()
    for dest in destinations:
        print(dest)
        dest_iata    = dest["iataCode"]
        target_price = float(dest["targetPrice"])
        deal = search_flight(dest_iata, target_price)
        if deal:
            send_alert(deal)
        else:
            print(f"No deal found for {dest_iata} (target ${target_price}).")