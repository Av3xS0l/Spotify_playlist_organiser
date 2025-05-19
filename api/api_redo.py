import dotenv as env
import spotipy
from spotipy.oauth2 import SpotifyOAuth

 # get las 5 songs
 # get playlist songs

 # padod song data objektu ieksa api clase
 # add song
 # remove song

class SongData:
    def __init__(self):

        self.currently_playing_type: str = '' # track, episode, or ad
        self.shuffle_state: bool = False #true or false
        self.song_progress_ms: int | None = None # int how much have you listened
        self.playlist_uri: str = ''
        self.playlist_id: str = ''
        self.playlist_name: str = ''
        self.playlist_owner_id: str = ''
        # self.playlist_collaborative = False # true or false 
        self.song_name: str = ''
        self.song_id: str = ''
        self.song_uri: str = ''
        self.song_artists: str = ''
        self.song_duration_ms: int | None = None  # int how long is the song
        self.song_image: str = ''


        self.last_5_songs: (T5) # type: ignore # track returns name, id, artist, album{ name, image }
    
    def is_track(self):
        if self.currently_playing_type == 'track':
            return True
        else:
            return False
    
    def playlist_info(self):
        # 0 = uri, 1 = id, 2 = name, 3 = collaborative, 4 = image url
        return (self.playlist_uri, self.playlist_id, self.playlist_name, self.playlist_collaborative)

    def song_info(self):
        # 0 = uri, 1 = id, 2 = name, 3 = artist name, 4 = image url
        return (self.song_uri, self.song_id, self.song_name, self.song_artists, self.song_image)

    def progress(self, treshold: float):
        try:
            proportion = self.song_progress_ms / self.song_duration_ms
            return proportion > treshold
        except ZeroDivisionError:
            return False
        


    


class Api: 
    def __init__(self):
        env.load_dotenv('.env')

        # iclude all scopes needed for api authentification
        scopes = ['user-library-read', 'user-read-playback-state', 'playlist-modify-public', 'playlist-modify-private', 'user-read-recently-played']
        scope = ' '.join(scopes)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        self.user_id: str = ''
        self.is_playing = False #true (if not paused) or false
        self.playlist_id = None
        self.playlist_set: set[str] = set()

        
    def api_call(self) -> SongData:
        song = SongData()

        user = self.sp.current_user()
        self.user_id = user['id']

        #last played songs
        n = 5
        recent = self.sp.current_user_recently_played(limit=n)
        self.recent_songs = recent['items']

        #general info based on playlist
        playback = self.sp.current_playback()
        if not playback:
            return None #nekas paslaik netiek atskanots
        
        song.currently_playing_type = playback['currently_playing_type'] # check if playing a track / music
        #song.is_playing = playback['is_playing'] # check if not paused
        song.shuffle_state = playback['shuffle_state'] # check if shuffle is enabled
        song.song_progress_ms = playback['progress_ms'] # how far has the song been listened

        #playlist info
        context = playback.get('context')
        
        if context and context['type'] == "playlist":
            song.playlist_uri = context['uri']
            song.playlist_id = song.playlist_uri.split(":")[-1]
            
            

            try:
                playlist = self.sp.playlist(song.playlist_id)
                if self.playlist_id == None:
                    self.playlist_id = song.playlist_id
                    for track in playlist['tracks']['items']:
                        self.playlist_set.add(track['track']['id'])
                song.playlist_name = playlist['name']
                song.playlist_owner_id = playlist['owner']['id']
                


            except spotipy.exceptions.SpotifyException:
                pass  # Playlist may not be accessible

        #song (track) info
        song.song_name = playback['item']['name']
        song.song_id = playback['item']['id']
        song.song_uri = playback['item']['uri']
        song.song_artists = playback['item']['artists'][0]['name']
        song.song_duration_ms = playback['item']['duration_ms']
        song.song_image = playback['item']["album"]['images'][2]['url']

        return song


    def is_users_playlist(self, song: SongData):
        if self.user_id == song.playlist_owner_id:
            return True
        else:
            return False
        
    def song_not_in_playlist(self, song: SongData):
        if song.song_id in self.playlist_set:
            return False # song is in the playlist
        return True # song is not in the playlist
            
    def add_song(self, song: SongData):
        return self.sp.playlist_add_items(song.playlist_id, song.song_id)
    
    def remove_song(self, song: SongData):
        return self.sp.playlist_remove_all_occurrences_of_items(song.playlist_id, song.song_id)
