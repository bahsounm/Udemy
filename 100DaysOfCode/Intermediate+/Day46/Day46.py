import os,sys
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Optional sanity check (should print something, not None)
print("SPOTIPY_CLIENT_ID:", os.getenv("SPOTIPY_CLIENT_ID"))

# --------------- Billboard Scraper ---------------
year_to_travel = input("What day would you like a playlist for? (YYYY-MM-DD): ")
BILLBOARD_ENDPOINT = f"https://www.billboard.com/charts/hot-100/{year_to_travel}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0"
}

response = requests.get(url=BILLBOARD_ENDPOINT, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

all_songs = soup.find_all(
    name="h3",
    class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 "
           "lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px "
           "u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line "
           "lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max"
)

top_100 = [song.get_text(strip=True) for song in all_songs]

# --------------- Spotify Auth ---------------
scope = "playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI")
))

# getting our information i beleived this will be used to help create a playlist
user = sp.current_user()

new_playlist = None
playlists = sp.current_user_playlists()
for playlist in playlists['items']:
        if "{} Billboard 100".format(year_to_travel).lower() not in playlist['name'].lower():
            new_playlist = sp.user_playlist_create(user=user["id"], name="{} Billboard 100".format(year_to_travel), public=True, description="Udemy Top 100 of any date you want")
            break
        else:
             print("This Play List already exsists")
             sys.exit()
              

new_playlist_id = new_playlist["id"]

# Searh for a song
spotify_uris= []
for song in top_100:
    try:
        result = sp.search(q="track:{} year:{}".format(song,year_to_travel[:4]), type="track", limit=1)["tracks"]["items"][0]["uri"]
        spotify_uris.append(result)
    except:
        print("{} not found".format(song))
        continue

# Add each song to the playlist
sp.playlist_add_items(new_playlist_id,spotify_uris)