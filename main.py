import pygame
from pygame.locals import *
from sys import exit
from os import system
from cell import Cell
from board import Board

system("cls")

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


pygame.init()
pygame.font.init()

icon = pygame.image.load('2048ico.ico')
pygame.display.set_icon(icon)

font = pygame.font.SysFont('Clear Sans', 75)

windowWidth = 675
windowHeight = 675

gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption("2048 by Patrick Russell no rights reserved")

gameWindow.fill((186, 172, 159))

# Set up board and cells
board = Board()
board.generateCell()
board.generateCell()

running = True
while running:
    gameWindow.fill((186, 172, 159))

    # Put all the cells on the screen
    for cell in board.cells:
        surf = pygame.Surface((150, 150))
        surf.fill(cell.getColour())

        if cell.number != 0:
            text = font.render(str(cell.number), False, cell.getText())
            text_rect = text.get_rect(center=(150/2, 150/2))
            
            surf.blit(text, text_rect)

        gameWindow.blit(surf, (cell.pos))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_g:
                board.generateCell()

            if event.key == K_RIGHT:
                board.rightArrow()
                board.generateCell()

            if event.key == K_UP:
                board.upArrow()
                board.generateCell()

            if event.key == K_DOWN:
                board.downArrow()
                board.generateCell()

            if event.key == K_LEFT:
                board.leftArrow()
                board.generateCell()
            
            if event.key == K_PAUSE:
                board.cheat()

    keys = pygame.key.get_pressed()

    pygame.display.flip()


pygame.quit()
exit()