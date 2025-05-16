from ui import Window
from api import Api
from api import SongData
import os
from time import sleep


def main() -> None:
    
    win = Window()
    R_CMD_H = 5
    SLEEP_SEC = 1
    HEIGHT_MIN = 20
        
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
    win.add('recent commands', 'Commands', 0, win.height-R_CMD_H, win.width, R_CMD_H)
    win.add('cover', 'Cover', win.width-35, 2, 0, 0) # Replace with proper api call

    # API Init
    api = Api()

    def drawLoop(image: str):

        win.objMap['cover'].convert(image)
        win.draw()


    # Main loop
    for i in range(5):
        '''
        1. Get current song
        2. checks
        2.1 is same song
        2.2 is user playlist
        2.3 is a track
        2.4 shuffle state
        3. if 
        '''
        current_song = api.api_call()
        drawLoop(image=current_song.song_image)
        sleep(SLEEP_SEC)


if __name__ == "__main__":
    main()
