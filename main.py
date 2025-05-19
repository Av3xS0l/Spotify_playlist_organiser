from ui import Window
from api import Api
from api import SongData
import os
from time import sleep


def main() -> None:
    
    win = Window()
    R_CMD_H: int = 5
    SLEEP_SEC: int = 5
    HEIGHT_MIN: int = 20

    SKIP_CNT_TRESHOLD: int = 3
    SKIP_TRESHOLD = 0.4
    ADD_TRESHOLD = 0.8

        
    # Prepearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')    # clear the screen

    print('\033[?25l')  # hide the cursor
    if (win.height < HEIGHT_MIN):
        # Tereminal size too small
        print('\033[31mTermināļa izmērs ir mazāks par 20 rindām\nNav iespējams atēlot visus elementus\nLūdzu palieliniet loga izmērus')
        os.system('pause')
        print('\033[0m')
        return
    elif (win.height <= 25):
        # Scaling will be strange
        print('\033[31mTermināļa izmērs nav lielāks par 25 rindām\nProgramma saturēs vizuālus artefaktus')
        os.system('pause')
        print('\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')

    # Init of the widgets on the screen 
    win.add('main', 'Widget', 0, 1, win.width, win.height-R_CMD_H-1)
    win.add('commands', 'Commands', 0, win.height-R_CMD_H, win.width, R_CMD_H)
    win.add('cover', 'Cover', win.width-35, 2, 0, 0) # Replace with proper api call

    # API Init
    api = Api()

    def drawLoop(image: str):

        win.objMap['cover'].convert(image)
        win.draw()

    prev_song = SongData()

    SkippedSongs: dict[str, int] = {}


    # Main loop
    while True:
        # get current song
        current_song = api.api_call()
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
            if api.song_not_in_playlist(prev_song) and prev_song != None:
                if prev_song.progress(ADD_TRESHOLD):
                    api.add_song(prev_song)
                    win.objMap['commands'].addCommand(f"{prev_song.song_name} was added to the playlist", win.offBuffer, 'green')

            # has the song been skipped early?
            if prev_song.song_id != '' and not prev_song.progress(SKIP_TRESHOLD):
                win.objMap['commands'].addCommand(f"{prev_song.song_name} was skipped early", win.offBuffer, 'yellow')
                if prev_song.song_id in SkippedSongs.keys():
                    SkippedSongs[prev_song.song_id] += 1
                    if SkippedSongs[prev_song.song_id] >= SKIP_CNT_TRESHOLD:
                        api.remove_song(prev_song)
                        SkippedSongs.pop(prev_song.song_id)
                        win.objMap['commands'].addCommand(f"Removed {prev_song.song_name} from playlist", win.offBuffer, 'red')
                else:
                    SkippedSongs.update({prev_song.song_id: 1})
            

            
        prev_song = current_song
        drawLoop(image=current_song.song_image)    
        sleep(SLEEP_SEC)


if __name__ == "__main__":
    main()
