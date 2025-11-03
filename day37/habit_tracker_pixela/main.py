import requests

from datetime import datetime

# -------------------- CONSTANTS -------------------- #
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "olaidehammed"       # 👈 Choose any username (must be unique)
TOKEN = "supersecuretoken123"   # 👈 Create your own secret token
GRAPH_ID = "graph1"             # 👈 ID for your graph (no spaces)

# -------------------- CREATE USER -------------------- #
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# # Uncomment this section only the first time to create your account.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# -------------------- CREATE GRAPH -------------------- #
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coding Habit Tracker",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora"   # available colors: shibafu, momiji, sora, ichou, ajisai, kuro
# }
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# -------------------- ADD PIXEL (Today's Progress) -------------------- #
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
#
today = datetime.now().strftime("%Y%m%d")
# print(f"Today's date: {today}")
# #
# pixel_data = {
#     "date": today,
#     "quantity": input("How many hours did you code today? 👩‍💻 "),
# }
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# -------------------- UPDATE PIXEL -------------------- #
# If you want to update a record for today, use PUT.
update_endpoint = f"{pixel_creation_endpoint}/{today}"
new_data = {
    "quantity": input("How many hours did you code today? 👩‍💻 ")
}
response = requests.put(url=update_endpoint, json=new_data, headers=headers)
print(response.text)

# -------------------- DELETE PIXEL -------------------- #
# delete_endpoint = f"{pixel_creation_endpoint}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)