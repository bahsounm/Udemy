
import os
from twilio.rest import Client
TWILIO_ID = os.environ.get("TWILIO_ID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")

class NotificationManager:
    def __init__(self):
        self.auth = TWILIO_AUTH
        self.id = TWILIO_ID

    def notify(self):
        client = Client(self.id, self.auth)
        message = client.messages.create(
            body="Testing",
            from_="+18142819918",
            to="+19055509496",
        )