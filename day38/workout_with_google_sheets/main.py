import requests
from datetime import datetime

# -------------------- NUTRITIONIX CONFIG -------------------- #
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "16cca952" #a6ae0339
API_KEY = "3283d972d9db04180182bf840188a789" #d13a5e8432bd0b05d749b49709b6808f

# -------------------- SHEETY CONFIG -------------------- #
SHEETY_ENDPOINT = "https://api.sheety.co/cfe410972db5adc5401fb03798265f66/workouts/sheet1"
TOKEN = "adfsdugihkdjlmhsjbklzklmjnchbjjkzklNBgzchvgj"

# -------------------- USER INPUT -------------------- #
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 175,
    "age": 27
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()
print(result)

# -------------------- ADD TO GOOGLE SHEET -------------------- #
# today = datetime.now()
# date = today.strftime("%Y-%m-%d")
# time = today.strftime("%H:%M:%S")
#
# sheety_headers = {
#     "Authorization": f"Bearer {TOKEN}"
# }
#
# for exercise in result["exercises"]:
#     sheet_input = {
#         "workout": {
#             "date": date,
#             "time": time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
#     sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, headers=sheety_headers)
#     print(sheet_response.text)