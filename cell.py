from pygame import image
import os

class Cell:
    def __init__(self, pos, number):
        self.pos = pos
        self.number = number
    
    def getColour(self):

        colourDict = {
        0: (204,192,179),
        2: (238,228,218),
        4: (234,224,200),
        8: (242,177,121),
        16: (245,149,99),
        32: (246,124,95),
        64: (246,94,59),
        128: (237,207,114),
        256: (237,204,97),
        512: (237,200,80),
        1024: (237,196,63),
        2048: (233,197,0)
        }

        if self.number <= 2048:
            return colourDict[self.number]
        else:
            return colourDict[2048]
    
    def getText(self):
        textColourDict = {
            "dark": (120, 112, 101),
            "light": (255, 255, 255)
        }

        if self.number < 8:
            return textColourDict["dark"]
        else:
            return textColourDict["light"]
    
    def getDigits(self):
        if self.number < 10:
            return 1
        if self.number < 100:
            return 2
        if self.number < 1000:
            return 3
        if self.number < 10000:
            return 4