'''
Main UI driver for the app.
Handles all of the user input and toggles.
Shows the previous commands and lets user access the
'''

import os
# class UI:
#     def __init__(self, title: str = 'A simple UI'):
#         self._size = os.get_terminal_size(1)
#         self.WIDTH: int = self._size.columns
#         self.HEIGHT: int = self._size.lines - 1 # !!!! TESTING !!!!
#         self._frame: list = [0]*self.HEIGHT*self.WIDTH
#         self._clearcmd = 'cls' if os.name == 'nt' else 'clear'
#         self._CMD_HEIGHT = 4  # height of the command window

#         self.title: str = title


#     def renderFrame(self) -> None:
#         os.system(self._clearcmd)
        
#         # draw the main frame and the lowwer command window
#         print(f'╭{"─"*(len(self.title)+4)}┬{"─"*(self.WIDTH-(len(self.title)+7))}╮')
#         # render title bar
#         print(f'├─ {self.title} ─╯{" "*(self.WIDTH-6-len(self.title))}│')

#         for i in range(self.HEIGHT-self._CMD_HEIGHT-3):
#             print(f'│{" "* (self.WIDTH-2)}│')
#         print(f'╰{"─"*(self.WIDTH-2)}╯')
#         print(f'╭{"─"*(self.WIDTH-2)}╮')
#         for i in range(self._CMD_HEIGHT):
#             print(f'│{" "* (self.WIDTH-2)}│')
#         print(f'╰{"─"*(self.WIDTH-2)}╯')


# obj = UI()
# obj.renderFrame()


# # os.system('pause')