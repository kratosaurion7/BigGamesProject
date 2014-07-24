import pygame, sys
from pygame import *

import Rectangle
from Rectangle import *

class Game():
    pygame.init()

    gameObjects = []

    surfaceHeight = 600
    surfaceWidth = 800

    paddleWidth = 150
    paddleHeight = 25

    drawSurface = pygame.display.set_mode((surfaceWidth, surfaceHeight))

    rec = DrawRectangle()

    rec.Color = (0, 255, 0)
    rec.Height = paddleHeight
    rec.Width = paddleWidth
    rec.X = 10
    rec.Y = 10

    rec2 = DrawRectangle()

    rec2.Color = (0, 255, 0)
    rec2.Height = paddleHeight
    rec2.Width = paddleWidth
    rec2.X = 10
    rec2.Y = 400

    gameObjects.append(rec)
    gameObjects.append(rec2)

    def Start(self):
        while True:
            for event in pygame.event.get():
                self.HandleEvent(event)

            self.Update()

            self.Draw()
            
    def Draw(self):
        self.drawSurface.fill((0, 0, 0))
        # Iterate and draw surface objects

        for obj in self.gameObjects:
            self.DrawObject(obj, self.drawSurface)

        pygame.display.update()

    def Update(self):
        # Iterate and update surface objects
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] == True:
            self.rec.X += 1
            self.rec.X = self.ClampValue(self.rec.X, 0, self.surfaceWidth - self.paddleWidth)
        if keys[K_LEFT] == True:
            self.rec.X -= 1
            self.rec.X = self.ClampValue(self.rec.X, 0, self.surfaceWidth - self.paddleWidth)
        if keys[K_d] == True:
            self.rec2.X += 1
            self.rec2.X = self.ClampValue(self.rec2.X, 0, self.surfaceWidth - self.paddleWidth)
        if keys[K_a] == True:
            self.rec2.X -= 1
            self.rec2.X = self.ClampValue(self.rec2.X, 0, self.surfaceWidth - self.paddleWidth)

    def HandleEvent(self, event):
        if event.type == QUIT:
            pygame.quit()

    def DrawObject(self, object, surface):
        objectSurface = Surface((object.Width, object.Height))
        objectSurface.fill(object.Color)
        surface.blit(objectSurface, (object.X, object.Y))


    def ClampValue(self, currentValue, minValue, maxValue):
        if currentValue > maxValue:
            return maxValue
        elif currentValue > minValue & currentValue < maxValue:
            return currentValue
        elif currentValue <= minValue:
            return minValue