import os
import requests
from flight_data import FlightData

SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_GET_ENPOINT = "https://api.sheety.co/247e75aa2439b0d8bf6b9e44d3031a5f/flightDeals/prices"
SHEETY_PUT_ENDPOINT = "https://api.sheety.co/247e75aa2439b0d8bf6b9e44d3031a5f/flightDeals/prices/"
class DataManager:
    def __init__(self):
        self.auth = SHEETY_AUTH
        self.endpoint = SHEETY_GET_ENPOINT


    def get_prices(self):
        current_flight_prices = {}

        response = requests.get(url=SHEETY_GET_ENPOINT)
        response.raise_for_status()
        data = response.json()["prices"]

        for city in data:
            current_flight_prices[city["iataCode"]] = [city["id"], city["lowestPrice"]]
        return current_flight_prices
    

    def set_new_prices(self, flights):
        for code in flights:
            flight = flights[code]
            new_data = {
                "price":{
                    "lowestPrice":flight.price,
                    "originAirport":flight.origin_airport,
                    "destinationAirport":flight.destination_airport,
                    "departDate":flight.out_date,
                    "returnDate":flight.return_date,
                    "airline":flight.airline
                }
            }
            response = requests.put(url=SHEETY_PUT_ENDPOINT+str(flight.id), json=new_data)
            response.raise_for_status()
            print("done")
        

    def get_iata_codes(self):
        codes = []

        response = requests.get(url=SHEETY_GET_ENPOINT)
        response.raise_for_status()
        data = response.json()["prices"]

        for city in data:
            codes.append(city["iataCode"])
    
        return codes
