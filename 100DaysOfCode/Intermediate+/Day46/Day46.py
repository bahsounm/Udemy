import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
# import requests
# from bs4 import BeautifulSoup

# # year_to_travel = input("What year would you like to travel to (YYYY-MM-DD)?: ")
# year_to_travel = "2002-07-09"
# BILLBOARD_ENDPOINT  = "https://www.billboard.com/charts/hot-100/{}".format(year_to_travel)

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0"
# }

# response = requests.get(url=BILLBOARD_ENDPOINT, headers=headers)
# response.raise_for_status()
# data = response.text

# soup = BeautifulSoup(data, "html.parser")

# all_songs = soup.find_all(name="h3", class_='c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max')

# top_100 = []
# for song in all_songs:
#     top_100.append((song.getText()).replace('\n', '').replace('\t', '').strip())

# print(top_100)

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


