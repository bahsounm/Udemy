class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, airline, currency, duration):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.airline = airline
        self.currency = currency
        self.duration = duration
        self.id = 0
    
    def set_id(self, id):
        self.id = id
