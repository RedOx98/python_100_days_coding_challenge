import requests
from tkinter import *
from tkinter import messagebox


# ---------------------------- CONSTANTS ------------------------------- #
API_KEY = "3583838358de74ac91f9f1ba65e9c115"  # 👈 Replace this with your OpenWeatherMap API key
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# ---------------------------- FETCH WEATHER --------------------------- #
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        print(data)

        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        result_label.config(
            text=f"🌍 {city_name}\n🌡️ Temp: {temperature}°C\n☁️ {description}\n💧 Humidity: {humidity}%"
        )

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Weather App")
window.config(padx=30, pady=30, bg="#87CEEB")

title_label = Label(text="☀️ OpenWeather App", font=("Arial", 18, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=10)

city_entry = Entry(width=30, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

search_button = Button(text="Get Weather", command=get_weather, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
search_button.pack(pady=10)

result_label = Label(text="", font=("Arial", 14), bg="#87CEEB", fg="#333")
result_label.pack(pady=20)

window.mainloop()