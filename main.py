import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env_file_path")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")

REDIRECT_URL = "http://127.0.0.1:8888/callback"


# Get the date from the user
date = input("Which year do you want to travel to?\nType date in this format YYYY-MM-DD: ")

# Fetch the songs from Billboard
header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)

soup = BeautifulSoup(response.text, "html.parser")
topMusics = []
topMusics_ul = soup.find_all(name="ul", class_="o-chart-results-list-row")

for song in topMusics_ul:
    song_tag = song.find(name="h3", id="title-of-a-story")
    if song_tag:
        text = song_tag.getText()
        text = text.replace('\t','').replace('\n','')
        topMusics.append(text)

# Connect to Spotify
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,)
    )
user_id = sp.current_user()["id"]

# Search for the songs in Spotify
song_uris = []
year = date.split("-")[0]
for song in topMusics:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Create a playlist 
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} BillBoard 100",
    public=False,
    description=f"Top 100 songs from {date}"
)

# Add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"],
                      items=song_uris)
print("playlist created successfully!")
