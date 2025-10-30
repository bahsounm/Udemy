import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import smtplib

TWILIO_ID = os.environ.get("TWILIO_ID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("MY_PASS")

class NotificationManager:
    def __init__(self):
        self.auth = TWILIO_AUTH
        self.id = TWILIO_ID

    def notify_by_phone(self, flights):
        for code in flights:
            flight = flights[code]
            client = Client(self.id, self.auth)
            message = client.messages.create(
                body="Low Price alert! Only ${} to fly to {} on {} until {}".format(flight.price,code, flight.out_date, flight.return_date),
                from_="+18142819918",
                to="+19055509496",
            )
    def notify_by_email(self,flights, users):
        # create the message
        msg = ""
        for code in flights:
            flight = flights[code]
            msg += "Low Price alert! Only ${} to fly to {} on {} until {}".format(flight.price,code, flight.out_date, flight.return_date) + "\n"

        if msg == "":
            return
        for user in users:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=users[user]["email"], msg="Subject:New Flights Found\n\nHey{} {},\nHere are the new Flights we found \n\n{}".format(users[user]["firstname"], users[user]["lastname"],msg))