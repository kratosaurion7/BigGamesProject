import pygame, sys
from pygame import *

xCoord = 0
yCoord = 0

move = False;

def MoveRight():
    global xCoord
    xCoord += 1

pygame.init()

xsurface = pygame.display.set_mode((800, 600))

rec = Surface((50, 50))

rec.fill((0, 255, 0))

pygame.display.set_caption("WINDOWZ")

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            move = True
        if event.type == KEYUP:
            move = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if move:
        MoveRight()

    xsurface.fill((0, 0, 0))
    xsurface.blit(rec, (xCoord, yCoord))
    pygame.display.update()