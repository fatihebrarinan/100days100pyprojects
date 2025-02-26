from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#This program is not 100% accurate.

input_date = input("Which year's trend songs you want to include in your playlist? (Format = YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{input_date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
title_list = [item.getText().strip() for item in soup.select("li ul li h3")]
singer_list = [item.getText().strip() for item in soup.select("li ul li span.a-font-primary-s")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True
))

uri_list = []

for title in title_list:
    current_index = title_list.index(title)
    try:
        result = sp.search(q=f" track: {title_list[current_index]} artist: {singer_list[current_index]} year: {input_date.split("-")[0]}",
                           type="track",
                           market="US")
        if result["tracks"]["items"]:
            uri_list.append(result["tracks"]["items"][0]["uri"])
        else:
            print(f"{title} not found.")
    except Exception as e:
        print(f"Error {e} occurred while finding {title}.")

if uri_list:
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"Billboard Popular 100 ({input_date})",
        public=False
    )
    sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
    print(f"Playlist created: {playlist['external_urls']['spotify']}")


