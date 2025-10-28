import os
import requests

SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_ENPOINT = "https://api.sheety.co/247e75aa2439b0d8bf6b9e44d3031a5f/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.auth = SHEETY_AUTH
        self.endpoint = SHEETY_ENPOINT


    def get_prices(self):
        pass

    def set_new_price(self):
        pass