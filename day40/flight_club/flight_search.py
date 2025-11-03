from amadeus import Client, ResponseError
from datetime import datetime, timedelta
from config import AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET

amadeus = Client(client_id=AMADEUS_CLIENT_ID, client_secret=AMADEUS_CLIENT_SECRET)

class FlightSearch:
    def get_flight_data(self, origin_iata, dest_iata):
        try:
            departure_date = (datetime.now() + timedelta(days=1)).date().isoformat()
            return_date = (datetime.now() + timedelta(days=14)).date().isoformat()

            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_iata,
                destinationLocationCode=dest_iata,
                departureDate=departure_date,
                returnDate=return_date,
                adults=1,
                currencyCode="USD",
                nonStop=True
            )
            if response.data:
                return response.data[0]  # cheapest flight
            else:
                return None
        except ResponseError as e:
            print("Error:", e)
            return None