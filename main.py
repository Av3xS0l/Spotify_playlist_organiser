from ui import Window
import os


def main() -> None:
    
    win = Window()
    R_CMD_H = 5

    # Prepearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')    # clear the screen

    print('\033[?25l')  # hide the cursor
    if (win.height < 20):
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
    win.add('album cover', 'Cover', win.width-35, 2, 0, 0, "https://i.scdn.co/image/ab67616d000048512a0a63a579994e303613c1f8") # Replace with proper api call
    


    # Main loop
    # 1. 
    # 2. 
    # 3. push command to the screen
    # x. Update the screen
    win.draw()

if __name__ == "__main__":
    main()
