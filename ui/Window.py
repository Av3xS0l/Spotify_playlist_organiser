'''
Main UI driver for the app.
Handles all of the user input and toggles.
Shows the previous commands and lets user access the
'''

import os
from .datatypes import CommandQueue
from PIL import Image
import requests as req
import io


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
        self.commands = CommandQueue(height-2)
    
    def addCommand(self, command: str, buff: list[str]) -> None:
        self.commands.add(command)
        self.frame(buff)


    def frame(self, buff: list[str]) -> None:
        buff[self.y] = buff[self.y][:self.x] + '╭' + '─'*(self.width-2) + '╮' + buff[self.y][self.x+self.width:]
        
        coms = self.commands.get()
    
        for i in range(self.y+1, self.y+self.height-1):
            text = coms[i-(self.y+1)] if coms[i-(self.y+1)] != None else '' 
            buff[i] = buff[i][:self.x] + ' '*(self.width-2) + buff[i][self.x+self.width:]
            middle = text+buff[i][self.x + len(text):self.x + self.width-2]
            buff[i] = buff[i][:self.x] + '│' + middle + '│' + buff[i][self.x+self.width:]
        
        buff[self.y+self.height-1] = buff[self.y+self.height-1][:self.x] +'╰' + '─'*(self.width-2) + '╯' + buff[self.y+self.height-1][self.x+self.width:]


class Cover(Widget):
    '''
    !!IMPORTANT!!
    Width = 32+2 (34), Height = 16+2 (18)
    '''
    def __init__(self, name: str, x: int, y: int, width: int = 34, height: int = 18) -> None:
        super().__init__(name, x, y, width, height)
        self.pixels = [" "*32]*16

    def convert(self, link: str | None):
        '''
        link: spotify 64x64 iamge url
        ['item']["album"]['images'][2]['url']
        '''
        if link is None:
            return
        imgData = req.get(link).content
        img = Image.open(io.BytesIO(imgData)).resize((self.height-2,self.height-2)).convert('RGB')
        for y in range(self.height-2):
            line = []
            for x in range(self.height-2):
                r, g, b = img.getpixel((x, y))
                esc = f"\x1b[38;2;{r};{g};{b}m"
                line.append(f"{esc}██")
            self.pixels[y] = ''.join(line) + "\x1b[0m"

    def frame(self, buff: list[str]) -> None:
        buff[self.y] = buff[self.y][:self.x] + '╭' + '─'*(self.width-2) + '╮' + buff[self.y][self.x+self.width:]
           
    
        for i in range(self.y+1, self.y+self.height-1):
            middle = self.pixels[i-(self.y+1)]
            buff[i] = buff[i][:self.x] + '│' + middle + '│' + buff[i][self.x+self.width:]
        
        buff[self.y+self.height-1] = buff[self.y+self.height-1][:self.x] +'╰' + '─'*(self.width-2) + '╯' + buff[self.y+self.height-1][self.x+self.width:]




class Window:
    '''
    A class to display a window in terminal
    '''
    
    def __init__(self) -> None:
        self.width, self.height = os.get_terminal_size()
        self.buffer: list[str] = [" "*self.width]*(self.height+1)
        self.offBuffer: list[str] = [" "*self.width]*(self.height+1)
        self.objMap: dict[str, Widget | Commands | Cover] = {}

    
    def draw(self):
        print('\033[H')
        for idx, line in enumerate(self.offBuffer):
            if line != self.buffer[idx]:
                # finds the common prefix of a string
                pref: int = len(os.path.commonprefix([self.buffer[idx], self.offBuffer[idx]]))
                print(f'\033[{idx};{pref+1}H'+self.offBuffer[idx][pref:])
                self.buffer[idx] = self.buffer[idx][:pref] + self.offBuffer[idx][pref:]
    
    def add(self, name: str, dtype: str, x: int, y: int, w: int, h: int, link: str | None = None) -> None:
        match dtype:
            case 'Widget':
                self.objMap[name] = Widget(name, x, y, w, h)
            case 'Commands':
                self.objMap[name] = Commands(name, x, y, w, h)
            case 'Cover': 
                self.objMap[name] = Cover(name, x, y)
                self.objMap[name].convert(link) # initial link. can later be updated by calling the same function
            case _:
                raise Exception("Unknown widget type")
        self.objMap[name].frame(self.offBuffer)

