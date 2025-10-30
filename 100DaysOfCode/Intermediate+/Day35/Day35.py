# API authentication
# From the open weather site

import requests
from twilio.rest import Client
api_key = "4aa131804a366fda3437957a77142b7c"
account_sid = "AC556c3903b9e863bb137220cddc6073e7"
auth_token = "28163782b6332b04d80e11261b042614"



# recov_code = "RZ9C82ZLYV5HFCJ8G72KRWTW"

MY_LAT = 43.817245
MY_LONG = -79.119316

parameters = {"lat":MY_LAT, "lon":MY_LONG, "appid":api_key, "cnt": 4}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_="+18142819918",
        to="+19055509496",
)
    
print(message.status)
