import os
from dotenv import load_dotenv
load_dotenv()

from twitter_bot import TwitterBot

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

PROMISED_DOWN = 150
PROMISED_UP = 50

bot = TwitterBot(PROMISED_DOWN, PROMISED_UP)

found_speeds = bot.get_internet_speed()

if found_speeds:
    bot.tweet_at_provider(found_speeds, TWITTER_EMAIL, TWITTER_PASSWORD)
else:
    print("Speeds are as promised")
