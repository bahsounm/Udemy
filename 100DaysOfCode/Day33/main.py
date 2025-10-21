import requests
from datetime import datetime
import smtplib

MY_LAT = 43.816532
MY_LNG = -79.120615

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
if MY_LAT < iss_latitude +5 and MY_LAT > iss_latitude-5 and MY_LNG < iss_longitude +5 and MY_LNG > iss_latitude-5:
# and it is currently dark
    if time_now.hour < sunrise or time_now.hour > sunset:
# Then send me an email to tell me to look up.
        MY_EMAIL = "hassunaBazuna02@gmail.com"
        MY_PASS = "zjubmrjulerkhqcf"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: THE ISS IS HERE\n\nGo outside and look up the ISS is there RIGHT NOW")
# BONUS: run the code every 60 seconds.



