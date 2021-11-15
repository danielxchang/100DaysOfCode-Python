import datetime as dt
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv


load_dotenv()

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "https://example.com"


def choose_date():
    while True:
        past = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        try:
            year, month, day = map(int, past.split("-"))
            dt.date(year=year, month=month, day=day)
        except ValueError:
            print("Enter a valid date.")
        else:
            return past


def scrape_billboard(date):
    url = f"{BILLBOARD_ENDPOINT}/{date}"
    response = requests.get(url)
    billboard_html = response.text
    soup = BeautifulSoup(billboard_html, "html.parser")
    song_tags = soup.find_all(class_="chart-element__information__song")
    artist_tags = soup.find_all(class_="chart-element__information__artist")
    songs = [song.getText() for song in song_tags]
    artists = [artist.getText() for artist in artist_tags]
    billboard_hot_100 = {
        i + 1: {
            "song": songs[i],
            "artist": artists[i]
        } for i in range(len(songs))
    }
    return billboard_hot_100


def create_playlist(date, songs):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="playlist-modify-private"))
    results = sp.current_user()
    user_id = results['id']
    playlist = sp.user_playlist_create(user_id, f"{date}: Billboard Hot 100", public=False)
    playlist_id = playlist['id']
    year = date.split("-")[0]

    track_uris = []
    for song in songs.values():
        track = song['song']
        artist = song['artist']
        query = f"track:{track} artist:{artist} year:{year}"
        track_info = sp.search(q=query, type="track")

        try:
            uri = track_info['tracks']['items'][0]['uri']
        except IndexError:
            continue
        else:
            track_uris.append(uri)

    sp.playlist_add_items(playlist_id, track_uris)


def spotify_time_machine():
    date = choose_date()
    bb_hot_100 = scrape_billboard(date)
    create_playlist(date, bb_hot_100)
    print("Playlist has been created!")


if __name__ == "__main__":
    spotify_time_machine()