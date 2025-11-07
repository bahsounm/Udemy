from driver_manager import DriverManager



ff = DriverManager()

responses = ff.get_properties()

ff.fill_form(responses=responses)