import os
import requests


AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")

parameters = {
    "grant_type": "client_credentials",
    "client_id": "ppNXtOcRs6wCu0ccmLZy5ugkHBCUPpqJ",
    "client_secret": "saH1ajxHBZjmVL7L"
}

response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", data=parameters, headers={"Content-Type":"application/x-www-form-urlencoded"})
response.raise_for_status()
print(response.json()["access_token"])