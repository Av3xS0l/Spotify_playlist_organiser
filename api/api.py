import dotenv as env
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = env.get_key('.env', 'SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = env.get_key('.env', 'SPOTIPY_CLIENT_SECRET')

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])