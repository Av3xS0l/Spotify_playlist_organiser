import os
import dotenv as env
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 2.1. Iegūst dziesmu, kas pašreiz skan.  - done
# 2.2. Iegūt playlisti, kas pašreiz skan  - done
# vai dziema noklausita vismaz lidz pusei - done
# 2.3. Iegūst, vai šobrīd skan shuffle  - get if song is from the playlist - limit 100 songs due to api - done
# 2.4. Iegūst pēdējās N dziesmas - done
# 2.5. determines if skiped
class api: 
    def __init__(self):
        env.load_dotenv('.env')

        # iclude all scopes needed for api authentification
        scopes = ['user-library-read', 'user-read-playback-state', 'playlist-modify-public', 'playlist-modify-private', 'user-read-recently-played']
        scope = ' '.join(scopes)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def current_playlist(self):
        playback = self.sp.current_playback()
        context = playback.get('context')

        playlist_uri = context['uri']
        playlist_id = playlist_uri.split(':')[-1] #extract playlist id
        playlist_info = self.sp.playlist(playlist_id) 
        print(f"Currently playing playlist: {playlist_info['name']}")
        print(f"Playlist ID: {playlist_id}")

        #return tuple, bc uses less space and is faster, we have predetermined nr of elements to return
        return(playlist_info, playlist_id, playlist_uri) 

    def current_song(self):
        result = self.sp.current_user_playing_track()

        song = result['item']
        song_name = song['name']
        song_artist = song['artists'][0]['name']
        song_id = song['id']
        print(f"Currently playing: {song_artist} - {song_name} - {song_id}")

        return(song_name, song_artist, song_id)


    def half_not_listened(self): #return true or false
        result = self.sp.current_playback()

        song = result['item']

        
        progress_ms = result.get('progress_ms', 0) #get mili secons
        duration_ms = song.get('duration_ms', 1)

        def ms_to_mmss(ms): #convert to pretty
            minutes = (ms // 1000) // 60 
            seconds = (ms // 1000) % 60
            return f"{minutes}:{str(seconds).zfill(2)}"

        progress_mmss = ms_to_mmss(progress_ms)
        duration_mmss = ms_to_mmss(duration_ms)
        percent = (progress_ms / duration_ms) * 100


        print(f"Currently playing: {song['name']} by {song['artists'][0]['name']}")
        print(f"Progress: {progress_mmss} / {duration_mmss} ({percent:.1f}%)")

        if percent < 50:
            return True
        else:
            return False
        
    def is_song_in_playlist(self):
        playback = self.sp.current_playback()
        context = playback.get('context')
        current_track = playback.get('item')

        if context and context['type'] == 'playlist':
            playlist_uri = context['uri']
            playlist_id = playlist_uri.split(':')[-1]

            # Fetch the playlist details
            playlist = self.sp.playlist(playlist_id)
            playlist_tracks = playlist['tracks']['items']

            # Check if the current track ID matches any track in the playlist
            for item in playlist_tracks:
                track = item['track']
                if track and track['id'] == current_track['id']:
                    print("Current track is from the playlist.")
                    return True
            print("Current track is NOT from the playlist.")
            return False
        else:
            print("No playlist context is currently active.")
            return False
        
    def last_n_songs(self):
        n = 5
        results = self.sp.current_user_recently_played(limit=n)
        songs = results['items']
        
        for idx, item in enumerate(songs, start=1):
            song = item['track']
            song_name = song['name']
            song_artist = song['artists'][0]['name']
            print(f"{idx}. {song_artist} - {song_name}")
        
        return songs
    
   # def skipped (self):






#def add_song(self):



# def is_shuffle():

# def last_n():

# def half_not_listened():

if __name__ == "__main__":
    spotify_api = api()
    #spotify_api.current_playlist
    spotify_api.current_song()
    spotify_api.half_not_listened()
    spotify_api.is_song_in_playlist()
    spotify_api.last_n_songs()