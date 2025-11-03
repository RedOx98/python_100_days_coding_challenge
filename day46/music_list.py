import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

date = input("which year do you wanna travel to? Type the date in this format YYYY-MM-DD: ")

year = date.split("-")[0]

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url, headers=header)
music_res = response.text
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(f"Found {len(song_names)} songs from {date} 🎵")

# ----------------- SPOTIFY AUTH ----------------- #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.google.com",
        client_id="ac635b9af3c14792811f1a1595462e84",
        client_secret="f1e85cc5e23141618d2667cb2b21e0b2",
        show_dialog=True,
        cache_path="token.txt",
        username="hammed ridwan"
    )
)



user_id = sp.current_user()["id"]
print(user_id)

# ----------------- SEARCH SONGS ON SPOTIFY ----------------- #
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"❌ {song} not found on Spotify. Skipped.")

# ----------------- CREATE PLAYLIST ----------------- #
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 songs from {date}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"✅ Playlist '{playlist['name']}' created successfully with {len(song_uris)} songs!")

