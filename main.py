from ui import Window
from api import Api
from api import SongData
import os
from time import sleep
import pickle


def main() -> None:
    # Set up environment
    win = Window()
    R_CMD_H: int = 5
    SLEEP_SEC: int = 5
    HEIGHT_MIN: int = 25

    SKIP_CNT_TRESHOLD: int = 2
    SKIP_TRESHOLD: float = 0.4
    ADD_TRESHOLD: float = 0.8

        
    # Prepearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')    # clear the screen

    print('\033[?25l')  # hide the cursor

    if (win.height < HEIGHT_MIN):
        # Tereminal size too small
        print(f'\033[31mTermināļa izmērs ir mazāks par {HEIGHT_MIN} rindām\nNav iespējams atēlot visus elementus\nLūdzu palieliniet loga izmērus')
        os.system('pause')
        print('\033[0m')
        return

    # Init of the widgets on the screen 
    win.add('main', 'Widget', 0, 1, win.width, win.height-R_CMD_H-1)
    win.add('commands', 'Commands', 0, win.height-R_CMD_H, win.width, R_CMD_H)
    win.add('cover', 'Cover', win.width-35, 2, 0, 0) # Replace with proper api call
    win.add('info', 'Info', 1, 2, 32, 7)

    # API Init
    api = Api()

    # Draw the objects on the screen
    def drawLoop(image: str, data: tuple[str, str, str] | None = None) -> None:
        win.objMap['cover'].convert(image)
        if data != None:
            win.objMap['info'].setPlaylist(data[0])
            win.objMap['info'].setSong(data[1])
            win.objMap['info'].setArtist(data[2])
        win.draw()



    prev_song = SongData()

    try:
        with open('skipped_songs.pkl', 'rb') as f:
            SkippedSongs: dict[str, int] = pickle.load(f)
    except :
        SkippedSongs: dict[str, int] = {}

    # Main loop
    while True:
        # get current song
        current_song = api.api_call()

        # if no song is playing
        if current_song == None:
            win.objMap['commands'].addCommand("No song is currently playing", win.offBuffer, 'red')
            drawLoop(image=None)    
            sleep(SLEEP_SEC)
            continue
        
        # song checks
        if current_song.song_id != prev_song.song_id and \
            api.is_users_playlist(current_song) and \
            current_song.is_track() and \
            current_song.shuffle_state:
            
            # song is different
            
            # is the song in playlist?
            if api.song_not_in_playlist(prev_song) and prev_song.song_id != '':
                if prev_song.progress(ADD_TRESHOLD):
                    api.add_song(prev_song)
                    win.objMap['commands'].addCommand(f"{prev_song.song_name} was added to the playlist", win.offBuffer, 'green')

            # has the song been skipped early?
            if prev_song.song_id != '' and not prev_song.progress(SKIP_TRESHOLD):

                win.objMap['commands'].addCommand(f"{prev_song.song_name} was skipped early", win.offBuffer, 'yellow')

                # adding song to the skipped ones and removing if needed
                if prev_song.song_id in SkippedSongs.keys():
                    SkippedSongs[prev_song.song_id] += 1
                    if SkippedSongs[prev_song.song_id] >= SKIP_CNT_TRESHOLD:
                        # remove song from the playlist
                        api.remove_song(prev_song)
                        SkippedSongs.pop(prev_song.song_id)
                        win.objMap['commands'].addCommand(f"Removed {prev_song.song_name} from playlist", win.offBuffer, 'red')
                else:
                    SkippedSongs.update({prev_song.song_id: 1})

                # save state to file
                with open('skipped_songs.pkl', 'wb') as f:
                    pickle.dump(SkippedSongs, f)
                    
        # update the song and screen
        prev_song = current_song
        drawLoop(image=current_song.song_image, data=(current_song.playlist_name, current_song.song_name, current_song.song_artists))    
        sleep(SLEEP_SEC)


if __name__ == "__main__":
    main()
