import os
import requests


AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")

parameters = {
    "grant_type": "client_credentials",
    "client_id": AMADEUS_API_KEY,
    "client_secret": AMADEUS_API_SECRET
}

response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", json=parameters, headers={"Content-Type":"application/x-www-form-urlencoded"})
response.raise_for_status()
print(response.json())