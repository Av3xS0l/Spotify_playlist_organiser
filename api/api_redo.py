import dotenv as env
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class api: 
    def __init__(self):
        env.load_dotenv('.env')

        # iclude all scopes needed for api authentification
        scopes = ['user-library-read', 'user-read-playback-state', 'playlist-modify-public', 'playlist-modify-private', 'user-read-recently-played']
        scope = ' '.join(scopes)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        self.user_id = None # string
        self.currently_playing_type = None #string: track, episode, or ad
        self.is_playing = False #true (if not paused) or false
        self.shuffle_state = False #true or false
        self.song_progress_ms = 0 # int how much have you listened
        self.playlist_uri = None # string
        self.playlist_id = None # string
        self.playlist_name = None # string
        self.playlist_owner_id = None # string
        self.playlist_collaborative = False # true or false
        self.playlist_images = None # string url
        self.song_name = None # string
        self.song_id = None # string
        self.song_uri = None # string
        self.song_artists = None # string
        self.song_duration_ms = 0 # int how long is the song
        self.song_images = None #string url

    def api_call(self):
        user = self.sp.current_user()
        self.user_id = user['id']

        playback = self.sp.current_playback()
        if not playback:
            return None #nekas paslaik netiek atskanots
        
        self.currently_playing_type = playback['currently_playing_type'] # check if playing a track / music
        self.is_playing = playback['is_playing'] # check if not paused
        self.shuffle_state = playback['shuffle_state'] # check if shuffle is enabled
        self.song_progress_ms = playback['progress_ms'] # how far has the song been listened

        #playlist info
        context = playback.get('context')
        
        if context and context['type'] == "playlist":
            self.playlist_uri = context['uri']
            self.playlist_id = self.playlist_uri.split(":")[-1]

            try:
                playlist = self.sp.playlist(self.playlist_id)
                self.playlist_name = playlist['name']
                self.playlist_owner_id = playlist['owner']['id']
                self.playlist_collaborative = playlist['collaborative']
                self.playlist_images = playlist['images'][2]['url']

            except spotipy.exceptions.SpotifyException:
                pass  # Playlist may not be accessible

        #song (track) info
        self.song_name = playback['item']['name']
        self.song_id = playback['item']['id']
        self.song_uri = playback['item']['uri']
        self.song_artists = playback['item']['artists'][0]['name']
        self.song_duration_ms = playback['item']['duration_ms']
        self.song_images = playback['item']["album"]['images'][2]['url']


    def is_users_playlist(self):
        if self.user_id == self.playlist_owner_id:
            return True
        else:
            return False

    def is_track(self):
        if self.currently_playing_type == 'track':
            return True
        else:
            return False

    # def not_paused(self): - alreday have true or false attribute - self.is_playing


    def playlist_info(self):
        return ()

    # def is_shufle_enabled(self):

    # def song_info(self):

    # def listened_time(self):
