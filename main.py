from ui import Window
import os
import time

def main() -> None:
    
    win = Window()
    R_CMD_H = 5

    # Prepearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')    # clear the screen

    print('\033[?25l')  # hide the cursor


    # Init of the widgets on the screen 
    win.add('main', 'Widget', 0, 1, win.width, win.height-R_CMD_H-1)
    win.add('recent commands', 'Commands',0, win.height-R_CMD_H, win.width, R_CMD_H)



    def eventLoop()-> None:
        win.draw()


if __name__ == "__main__":
    main()
