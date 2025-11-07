import datetime as dt
import calendar
from selenium.webdriver.common.by import By

class BookClass:
    def __init__(self, driver, date: dt.datetime):
        self.driver = driver
        self.date = date
        self.classes = {
            "Classes booked":0,
            "Waitlists joined":0,
            "Already booked/waitlisted":0
        }
        self.detailed_list = []

    def book_class(self, hour=18, days_from_now=5):
        wanted_hour = hour
        wanted_date = self.date + dt.timedelta(days=days_from_now)
        date_str = f"{calendar.month_name[int(wanted_date.month)]} {wanted_date.day}"

        for class_type in ["spin", "yoga", "hiit"]:
            class_id = f"class-card-{class_type}-{wanted_date.year}-{wanted_date.month}-{wanted_date.day}-{wanted_hour}00"
            try:
                booking_btn = self.driver.find_element(By.CSS_SELECTOR, f"#{class_id} button")
                status = booking_btn.text

                if status == "Booked":
                    print(f"Already Booked: {class_type.capitalize()} ({date_str})")
                    self.classes["Already booked/waitlisted"] += 1
                elif status == "Waitlisted":
                    print(f"Already Waitlisted: {class_type.capitalize()} ({date_str})")
                    self.classes["Already booked/waitlisted"] += 1
                elif status == "Join Waitlist":
                    booking_btn.click()
                    print(f"Joined Waitlist: {class_type.capitalize()} ({date_str})")
                    self.classes["Waitlists joined"] += 1
                    self.detailed_list.append("[New Waitlist] {} Class on {}".format(class_type.capitalize(), date_str))
                else:
                    booking_btn.click()
                    print(f"Booked: {class_type.capitalize()} ({date_str})")
                    self.classes["Classes booked"] += 1
                    self.detailed_list.append("[New Booking] {} Class on {}".format(class_type.capitalize(), date_str))

                break 

            except:
                print(f"{class_type.capitalize()} class not found on {date_str}")
                continue

    def verify_booking(self, wanted_days):
        self.driver.find_element(By.CSS_SELECTOR, value="#my-bookings-link").click()
        # expected = 0
        # found = 0
        # for (key, value) in self.classes.items():
        #     expected += value

        # Check for bookings
        # try:
        #     confirmed_bookings = self.driver.find_element(By.CSS_SELECTOR, value="#confirmed-bookings-section")
        #     found += len(confirmed_bookings)
        # except:
        #     print("Found No Booked Classes")
        
        # Check for Waitlist
        try:
            confirmed_waitlist = self.driver.find_elements(By.CSS_SELECTOR, value="#waitlist-section p")
            for sel in confirmed_waitlist:
                print(sel.text)
            found += len(confirmed_waitlist)
        except:
            print("Found No Waitlisted Classes")

        # print("--- VERIFICATION RESULT ---\nExpected: {}\nFound:{}".format(expected, found))
        # if expected == found:
        #     print("SUCCESS: All bookings have been verified")
        # else:
        #     print("OOPS there seems to be an issue verrifying yourr bookings")



    def print_summary(self):
        summ = "---- BOOKING SUMMARY ----\n"
        for (key, value) in self.classes.items():
            summ += "{}: {}\n".format(key,value)
        print(summ)
    
    def print_detailed_list(self):
        detailed_print = "--- DETAILED CLASS LIST ---\n"
        if self.detailed_list:
            for event in self.detailed_list:
                detailed_print += "- {}".format(event)
        
            print(detailed_print)
