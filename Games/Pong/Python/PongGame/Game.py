import pygame, sys
from pygame import *

class Game():
    pygame.init()

    gameObjects = []

    drawSurface = pygame.display.set_mode((800, 600))


    def Start():
        while True:
            for event in pygame.event.get():
                self.HandleEvent(event.type)

                self.Update()

                self.Draw()

            sys.exit()

        return

    def Init():



        return

    def Draw():
        drawSurface.fill((0, 0, 0))

        # Iterate and draw surface objects

        pygame.display.update()
        return
    def Update():
        # Iterate and update surface objects

        return
    def HandleEvent():
        if event.type == KEYDOWN:
            move = True
        if event.type == KEYUP:
            move = False
        if event.type == QUIT:
            pygame.quit()
        return