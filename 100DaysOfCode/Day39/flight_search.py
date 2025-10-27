import os, requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")

class FlightSearch:
    def __init__(self):
        self.client_id = AMADEUS_API_KEY
        self.client_secret = AMADEUS_API_SECRET
        self.auth = self.get_auth()


    def get_auth(self):
        auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_headers = {"Content-Type":"application/x-www-form-urlencoded"}
        amadeus_body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
            }
        
        response = requests.post(url=auth_endpoint, json=amadeus_body, headers=auth_headers)
        response.raise_for_status()
        data = response.json()