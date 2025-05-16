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

        self.user_id = '' # string
        self.currently_playing_type = '' #string: track, episode, or ad
        self.is_playing = False #true (if not paused) or false
        self.shuffle_state = False #true or false
        self.song_progress_ms = 0 # int how much have you listened
        self.playlist_uri = '' # string
        self.playlist_id = '' # string
        self.playlist_name = '' # string
        self.playlist_owner_id = '' # string
        self.playlist_collaborative = False # true or false
        self.playlist_images = '' # string url
        self.song_name = '' # string
        self.song_id = '' # string
        self.song_uri = '' # string
        self.song_artists = '' # string
        self.song_duration_ms = 0 # int how long is the song
        self.song_images = '' #string url

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
        # 0 = uri, 1 = id, 2 = name, 3 = collaborative, 4 = image url
        return (self.playlist_uri, self.playlist_id, self.playlist_name, self.playlist_collaborative, self.playlist_images)

    # def is_shufle_enabled(self): - - alreday have true or false attribute - self.shuffle_state

    def song_info(self):
        # 0 = uri, 1 = id, 2 = name, 3 = artist name, 4 = image url
        return (self.song_uri, self.song_id, self.song_name, self.song_artists, self.song_images)

    def listened_half(self):
        try:
            proportion = self.song_progress_ms / self.song_duration_ms
            return proportion > 0.5
        except ZeroDivisionError:
            return False
        
if __name__ == "__main__":
    a = api()
    a.api_call()
    print(a.is_users_playlist())
    print(a.is_track())
    print(a.playlist_info())
    print(a.song_info())
    print(a.listened_half())

