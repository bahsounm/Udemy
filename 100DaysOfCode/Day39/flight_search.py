import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")


class FlightSearch:
    def __init__(self):
        self.client_id = AMADEUS_API_KEY
        self.client_secret = AMADEUS_API_SECRET
        self.auth = self.get_auth()
        self.origin_iata_code = "YTO"

    def get_auth(self):
        auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
        amadeus_body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        response = requests.post(url=auth_endpoint, data=amadeus_body, headers=auth_headers)
        response.raise_for_status()
        data = response.json()
        return data["access_token"]

    def get_offers(self, dest_loc_code, dep_date, ret_date):
        search_parameters = {
            "originLocationCode": self.origin_iata_code,
            "destinationLocationCode": dest_loc_code,
            "departureDate": dep_date,
            "returnDate": ret_date,
            "adults": 1
        }

        search_headers = {
            "Authorization": f"Bearer {self.auth}"
        }

        search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        response = requests.get(url=search_endpoint, params=search_parameters, headers=search_headers)
        if response.status_code == 401:
            print("Token invalid or expired, re-authenticating...")
            self.auth = self.get_auth()
            search_headers["Authorization"] = f"Bearer {self.auth}"
            response = requests.get(url=search_endpoint, params=search_parameters, headers=search_headers)

        response.raise_for_status()
        data = response.json()
        print(data)


flight = FlightSearch()
flight.get_offers("TYO", "2025-10-28", "2025-11-03")
