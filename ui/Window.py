'''
Main UI driver for the app.
Handles all of the user input and toggles.
Shows the previous commands and lets user access the
'''

import os
from datatypes import *

# All of the hardcoded strings for ease of use

# Ansii color code
COLOR : int= 255

SET_CLEAR = "\033[0m"
def SET_FG_COL(x): return f"\033[38;5{x}m"
def SET_BG_COL(x): return f"\033[48;5{x}m"

class Widget:
    '''
    A class to display a widget in terminal
    '''

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def frame(self, buff: list[str]) -> str:
        buff[self.y] = buff[self.y][:self.x]+SET_FG_COL(COLOR)+'╭' + '─'*(self.width-2) + '╮' + SET_CLEAR + buff[self.y][self.x+self.width:]
        for i in range(self.y+1, self.y+self.height-1):
            buff[i] = buff[i][:self.x]+SET_FG_COL(COLOR)+'│' + buff[i][self.x:self.x+self.width-2] +'│' + SET_CLEAR+buff[i][self.x+self.width:]
        buff[self.y+self.height-1] = buff[self.y+self.height-1][:self.x]+SET_FG_COL(COLOR)+'╰' + '─'*(self.width-2) + '╯' + SET_CLEAR+buff[self.y+self.height-1][self.x+self.width:]


class Window:
    '''
    A class to display a window in terminal
    '''
    
    def __init__(self) -> None:
        self.width, self.height = os.get_terminal_size()
        self.cursor = Point(0, 0)
        self.buffer: list[str] = [" "*self.width]*self.height
        self.offBuffer: list[str] = []
        self.objMap = {}
       
       # widget initialization goes here
        self.objMap['main'] = Widget('main', 0, 0, self.width, self.height)
        self.objMap['main'].frame(self.buffer)
    
    def draw(self):
        for x in self.buffer:
            print(x)

    


win = Window()
win.draw()