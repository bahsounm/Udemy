# API: Application Program Interface

# sets of comands programs and fucntions that allow us to creat csoftware to interact with exernal systems
# think lkike nba sites, sites with data, weather sites, live proces of crypto

# we need to knowthe API endpoints and make API requests

import requests
import datetime as dt
# is is making a requst to the site to get the json data from the API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# different response codes
# In general 
    # 1xx = Hold on 
    # 2xx = Here you go 
    # 3xx = need persmisson go away 
    # 4xx = you screwed up 
response.raise_for_status() # built in error exception handling
data = response.json()
print(data)

# API requests can take parameters (if the API allows it)
MY_LAT = 43.816532
MY_LNG = -79.120615


params = {"lat":MY_LAT, "lng": MY_LNG, "formatted":0}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print("Sunrise = {}\nSunset = {}".format(sunrise,sunset))

time_now = dt.datetime.now()