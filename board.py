import pygame
from cell import Cell

class Board:
    def __init__(self):
        self.cells = []
        for y in range(15, 675, 165):
            for x in range(15, 675, 165):
                self.cells.append(Cell((x, y), 0))

    def generateCell(self):
        import random

        n = random.randint(1, 10)
        if n == 10:
            number = 4
        else:
            number = 2
        
        emptyCells = []
        for i, cell in enumerate(self.cells):
            if cell.number == 0:
                emptyCells.append(i)
        
        if len(emptyCells) != 0:
            index = random.choice(emptyCells)

            self.cells[index].number = number
    
    def leftArrow(self):
        for x in range(4):
            scalar = 4*x
            for i in range(1+scalar, 4+scalar, 1):
                if self.cells[i].number != 0:
                    n = i
                    for j in range(i-1, -1+scalar, -1):
                        if self.cells[j].number == 0 or self.cells[j].number == self.cells[i].number:
                            n = j
                        else:
                            break

                    if self.cells[n].number == 0:
                        self.cells[n].number = self.cells[i].number
                        self.cells[i].number = 0
                    
                    elif self.cells[n].number == self.cells[i].number and i != n:
                        self.cells[i].number = 0
                        self.cells[n].number *= 2
    
    def rightArrow(self):
        for x in range(4):
            scalar = 4*x
            for i in range(2+scalar, -1+scalar, -1):
                if self.cells[i].number != 0:
                    n = i
                    for j in range(i+1, 4+scalar, 1):
                        if self.cells[j].number == 0 or self.cells[j].number == self.cells[i].number:
                            n = j
                        else:
                            break

                    if self.cells[n].number == 0:
                        self.cells[n].number = self.cells[i].number
                        self.cells[i].number = 0
                    
                    elif self.cells[n].number == self.cells[i].number and i != n:
                        self.cells[i].number = 0
                        self.cells[n].number *= 2
    
    def upArrow(self):
        for x in range(4):
            scalar = x
            for i in range(0+scalar, 16+scalar, 4):
                if self.cells[i].number != 0:
                    n = i
                    for j in range(i-4, -4+scalar, -4):
                        if self.cells[j].number == 0 or self.cells[j].number == self.cells[i].number:
                            n = j
                        else:
                            break

                    if self.cells[n].number == 0:
                        self.cells[n].number = self.cells[i].number
                        self.cells[i].number = 0
                    
                    elif self.cells[n].number == self.cells[i].number and i != n:
                        self.cells[i].number = 0
                        self.cells[n].number *= 2

    
    def downArrow(self):
        for x in range(4):
            scalar = x
            for i in range(8+scalar, -4+scalar, -4):
                if self.cells[i].number != 0:
                    n = i
                    for j in range(i+4, 16+scalar, 4):
                        if self.cells[j].number == 0 or self.cells[j].number == self.cells[i].number:
                            n = j
                        else:
                            break

                    if self.cells[n].number == 0:
                        self.cells[n].number = self.cells[i].number
                        self.cells[i].number = 0
                    
                    elif self.cells[n].number == self.cells[i].number and i != n:
                        self.cells[i].number = 0
                        self.cells[n].number *= 2
        
    def cheat(self):
        self.cells[0].number = 4096
        self.cells[1].number = 8192
        self.cells[2].number = 16384
        self.cells[3].number = 32768
        self.cells[4].number = 2048
        self.cells[5].number = 1024
        self.cells[6].number = 512
        self.cells[7].number = 256
        self.cells[8].number = 16
        self.cells[9].number = 32
        self.cells[10].number = 64
        self.cells[11].number = 128
        self.cells[12].number = 8
        self.cells[13].number = 4
        self.cells[14].number = 2
        self.cells[15].number = 2




