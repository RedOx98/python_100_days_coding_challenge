import requests

# res = requests.get(url='http://api.open-notify.org/iss-now.json')
# res.raise_for_status()
# value = res.json()
# print(value)

MY_LAT = -27.0887
MY_LONG = -152.2161
params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
res = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
res.raise_for_status()
value = res.json()
print(value)