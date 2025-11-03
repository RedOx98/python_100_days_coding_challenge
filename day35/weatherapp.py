import requests
from twilio.rest import Client
from datetime import datetime
import os

# ---------------------------- SETUP ---------------------------- #
# You can load these from environment variables instead for safety
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "3583838358de74ac91f9f1ba65e9c115"  # Replace with your OpenWeatherMap key

# Coordinates of your location (e.g., Lagos, Nigeria)
MY_LAT = 6.5244
MY_LONG = 3.3792

# Twilio credentials
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID" #os.environ.get("TWILIO_SID")
TWILIO_AUTH = "YOUR_TWILIO_AUTH_TOKEN" #os.environ.get("TWILIO_AUTH")
TWILIO_PHONE = "+2349044698791"    #os.environ.get("TWILIO_PHONE")
MY_PHONE = "+2349036949353"     #os.environ.get("MY_PHONE")

# ---------------------------- FETCH WEATHER ---------------------------- #
def check_rain_forecast():
    """Checks if there will be rain in the next 12 hours (4 forecast periods)."""
    weather_params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "cnt": 4,  # next 12 hours (4 intervals of 3h)
    }

    try:
        response = requests.get(OWM_ENDPOINT, params=weather_params)
        response.raise_for_status()
        data = response.json()

        # Each 'weather' item contains a weather condition code (id)
        will_rain = False
        for forecast in data["list"]:
            condition_code = forecast["weather"][0]["id"]
            if condition_code < 700:
                will_rain = True
                break

        if will_rain:
            send_rain_alert()
        else:
            print(f"{datetime.now()} - No rain expected in the next 12 hours.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as e:
        print(f"Error fetching forecast: {e}")

# ---------------------------- TWILIO ALERT ---------------------------- #
def send_rain_alert():
    """Sends an SMS notification via Twilio when rain is forecast."""
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body="🌧 Rain Alert! It might rain in the next few hours. Don't forget your umbrella ☔️",
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(f"✅ Alert sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send Twilio SMS: {e}")

# ---------------------------- MAIN EXECUTION ---------------------------- #
if __name__ == "__main__":
    check_rain_forecast()
