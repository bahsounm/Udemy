import datetime as dt
from gym_bot import GymBot
from book_class import BookClass


ACCOUNT_EMAIL = "bahsoun@test.com"
ACCOUNT_PASSWORD = "0987654321"
GYM_URL = "https://appbrewery.github.io/gym/"
TODAYS_DATE = dt.datetime.now()


bot = GymBot(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, GYM_URL)
bot.login()

booker = BookClass(bot.driver, TODAYS_DATE)
booker.book_class(hour=18,days_from_now=5)
booker.book_class(hour=18,days_from_now=7)

booker.print_summary()
booker.print_detailed_list()