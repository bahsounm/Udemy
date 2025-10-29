import os
import requests
import datetime as dt
from dotenv import load_dotenv
load_dotenv()

from flight_data import FlightData

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

    def get_min_offer(self, dest_loc_code, dep_date, ret_date):
        search_parameters = {
            "originLocationCode": self.origin_iata_code,
            "destinationLocationCode": dest_loc_code,
            "departureDate": dep_date.replace("/", "-"),
            "returnDate": ret_date.replace("/", "-"),
            "adults": 1,
            "currencyCode": "CAD",
            "max": 1,  # only one offer returned
        }

        search_headers = {
            "Authorization": f"Bearer {self.auth}"
        }

        search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        response = requests.get(url=search_endpoint, params=search_parameters, headers=search_headers, timeout=30)
        response.raise_for_status()
        data = response.json().get("data", [])

        if not data:
            return None

        offer = data[0]  # the only one
        itinerary = offer["itineraries"][0]
        segments = itinerary["segments"]
        first_seg = segments[0]
        last_seg = segments[-1]

        return FlightData(
            price=offer["price"]["total"],
            origin_airport=first_seg["departure"]["iataCode"],
            destination_airport=last_seg["arrival"]["iataCode"],
            out_date=dep_date,
            return_date=ret_date,
            airline=first_seg["carrierCode"],
            currency=offer["price"]["currency"],
            duration=itinerary.get("duration"),
        )

    def find_cheapest_offer(self, dest_loc_code, step_days=1, start=0, window_days=30):
        results = {}
        best = None
        best_price = None

        current_date = dt.datetime.now() + dt.timedelta(days=start)

        for i in range(0, window_days, step_days):
            dep_dt = current_date + dt.timedelta(days=i)
            ret_dt = dep_dt + dt.timedelta(days=7)

            dep = dep_dt.strftime("%Y-%m-%d")
            ret = ret_dt.strftime("%Y-%m-%d")

            flight = self.get_min_offer(dest_loc_code, dep, ret)  # returns FlightData or None (with max=1)
            results[dep] = flight

            if flight:
                price = float(str(flight.price))  # price is usually a string
                if (best_price is None) or (price < best_price):
                    best_price = price
                    best = flight

        # return just the cheapest flight; if you also want the per-day map, return (best, results)
        return best
