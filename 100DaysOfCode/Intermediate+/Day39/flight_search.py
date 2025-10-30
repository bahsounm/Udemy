import os
import requests
import datetime as dt
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from flight_data import FlightData

load_dotenv()

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")


class FlightSearch:
    def __init__(self):
        self.client_id = AMADEUS_API_KEY
        self.client_secret = AMADEUS_API_SECRET

        # Reuse connections + auto-retry on flaky sandbox responses
        self.session = requests.Session()
        retry = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=0.6,                 # 0.6s, 1.2s, 2.4s
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

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
        r = self.session.post(auth_endpoint, data=amadeus_body, headers=auth_headers, timeout=(5, 45))
        r.raise_for_status()
        return r.json()["access_token"]

    def get_min_offer(self, dest_loc_code, dep_date, ret_date):
        params = {
            "originLocationCode": self.origin_iata_code,
            "destinationLocationCode": dest_loc_code,
            "departureDate": dep_date.replace("/", "-"),
            "returnDate": ret_date.replace("/", "-"),
            "adults": 1,
            "currencyCode": "CAD",
            "max": 1,  # only one offer returned (cheapest surfaced)
        }
        headers = {"Authorization": f"Bearer {self.auth}"}
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        # Try up to 3 times for this date (handles timeouts and 5xx)
        for attempt in range(3):
            try:
                resp = self.session.get(url, params=params, headers=headers, timeout=(5, 60))

                # token expired? refresh once and retry immediately
                if resp.status_code == 401:
                    self.auth = self.get_auth()
                    headers["Authorization"] = f"Bearer {self.auth}"
                    resp = self.session.get(url, params=params, headers=headers, timeout=(5, 60))

                # Let session-level retry handle most cases; if a flaky status still slips through, back off
                if resp.status_code in (500, 502, 503, 504, 429):
                    # manual backoff then retry loop
                    import time
                    time.sleep(0.6 * (2 ** attempt))
                    continue

                resp.raise_for_status()
                data = resp.json().get("data", [])
                if not data:
                    return None

                offer = data[0]  # max=1 -> only item
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

            except requests.exceptions.ReadTimeout:
                # read timed out -> backoff and retry
                import time
                time.sleep(0.6 * (2 ** attempt))
                continue

        # give up on this date after retries
        return None

    def find_cheapest_offer(self, dest_loc_code, step_days=7, start=0, window_days=182, trip_days=14):
        results = {}
        best = None
        best_price = None

        current_date = dt.datetime.now() + dt.timedelta(days=start)

        for i in range(0, window_days, step_days):
            print("Here")
            dep_dt = current_date + dt.timedelta(days=i)
            ret_dt = dep_dt + dt.timedelta(days=trip_days)  # <-- 2-week trip by default

            dep = dep_dt.strftime("%Y-%m-%d")
            ret = ret_dt.strftime("%Y-%m-%d")

            flight = self.get_min_offer(dest_loc_code, dep, ret)  # FlightData or None (max=1)
            results[dep] = flight

            if flight:
                p = float(flight.price)  # price comes as string -> compare numerically
                if (best_price is None) or (p < best_price):
                    best_price = p
                    best = flight

        return best
