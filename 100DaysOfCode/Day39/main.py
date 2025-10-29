from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_man = DataManager()
flight_search = FlightSearch()
notif_man = NotificationManager()


# Obtain the cheapest flgith based on the iata codes that we want from the google sheets
iata_codes = data_man.get_iata_codes()
current_flight_prices = data_man.get_prices()


cheapest_flights_found = {}
for code in iata_codes:
    cheapest_flight_found = flight_search.find_cheapest_offer(dest_loc_code = code, start=1)
    cheapest_flights_found[code] = cheapest_flight_found

# compare the prices and only keep the ones that need to change
for code in current_flight_prices:
    if float(current_flight_prices[code][1]) < float(cheapest_flights_found[code].price):
        del cheapest_flights_found[code]
    else:
        cheapest_flights_found[code].set_id(current_flight_prices[code][0])


data_man.set_new_prices(cheapest_flights_found)

