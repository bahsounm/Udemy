import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_ID = os.environ.get("TWILIO_ID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")

class NotificationManager:
    def __init__(self):
        self.auth = TWILIO_AUTH
        self.id = TWILIO_ID

    def notify(self, flights):
        for code in flights:
            flight = flights[code]
            client = Client(self.id, self.auth)
            message = client.messages.create(
                body="Low Price alert! Only ${} to fly to {} on {} until {}".format(flight.price,code, flight.out_date, flight.return_date),
                from_="+18142819918",
                to="+19055509496",
            )