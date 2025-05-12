'''
Main UI driver for the app.
Handles all of the user input and toggles.
Shows the previous commands and lets user access the
'''

import os
import datatypes as dt
import time


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
        buff[self.y] = buff[self.y][:self.x] + '╭' + '─'*(self.width-2) + '╮' + buff[self.y][self.x+self.width:]
    
        for i in range(self.y+1, self.y+self.height-1):
            buff[i] = buff[i][:self.x]+ '│' + buff[i][self.x:self.x+self.width-2] +'│' + buff[i][self.x+self.width:]
        
        buff[self.y+self.height-1] = buff[self.y+self.height-1][:self.x] + '╰' + '─'*(self.width-2) + '╯' + buff[self.y+self.height-1][self.x+self.width:]

class Commands(Widget):
    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        super().__init__(name, x, y, width, height)
        self.commands = dt.CommandQueue(height-2)
    
    def addCommand(self, command: str) -> None:
        self.commands.add(command)

    def frame(self, buff: list[str]) -> str:
        buff[self.y] = buff[self.y][:self.x] + '╭' + '─'*(self.width-2) + '╮' + buff[self.y][self.x+self.width:]
        
        coms = self.commands.get()
    
        for i in range(self.y+1, self.y+self.height-1):
            text = coms[i-(self.y+1)] if coms[i-(self.y+1)] != None else '' 
            buff[i] = buff[i][:self.x] + ' '*(self.width-2) + buff[i][self.x+self.width:]
            middle = text+buff[i][self.x + len(text):self.x + self.width-2]
            buff[i] = buff[i][:self.x] + '│' + middle + '│' + buff[i][self.x+self.width:]
        
        buff[self.y+self.height-1] = buff[self.y+self.height-1][:self.x] +'╰' + '─'*(self.width-2) + '╯' + buff[self.y+self.height-1][self.x+self.width:]


class Window:
    '''
    A class to display a window in terminal
    '''
    
    def __init__(self) -> None:
        self.width, self.height = os.get_terminal_size()
        self.cursor = dt.Point(0, 0)
        self.buffer: list[str] = [" "*self.width]*self.height
        self.offBuffer: list[str] = [" "*self.width]*self.height
        self.objMap: dict[str, Widget | Commands] = {}
       
        # widget initialization goes here
        self.objMap['main'] = Widget('main', 0, 0, self.width, self.height-5)
        self.objMap['main'].frame(self.offBuffer)

        # widget for outputing recent calls
        self.objMap['output'] = Commands('output', 0, self.height-5, self.width, 5)

        self.objMap['output'].addCommand('test')
        self.objMap['output'].addCommand('test2')
        self.objMap['output'].addCommand('test3')
        
        self.objMap['output'].frame(self.offBuffer)


    
    def draw(self):
        for idx, line in enumerate(self.offBuffer):
            if line != self.buffer[idx]:
                # finds the common prefix of a string
                pref: int = len(os.path.commonprefix([self.buffer[idx], self.offBuffer[idx]]))
                print(f'\033[{idx};{pref+1}H'+self.offBuffer[idx][pref:])
                self.buffer[idx] = self.buffer[idx][:pref] + self.offBuffer[idx][pref:]
                