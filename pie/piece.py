import pygame
import math
from pygame.font import Font

class Piece():
    def __init__(self,
                 screen,
                 centerx, centery,
                 radius,
                 startAngle, stopAngle,
                 lineWidth):
        self.screen = screen
        self.center = centerx, centery
        self.radius = radius
        self.startAngle = startAngle
        self.stopAngle = stopAngle
        self.rect = self.getRect(self.center[0], self.center[1], radius, startAngle, stopAngle)
        self.lineWidth = lineWidth


    def getRect(self, centerx, centery, radius, startAngle, stopAngle):
        return centerx-radius, centery-radius, 2*radius, 2*radius

    def draw(self, color):
        pygame.draw.arc(self.screen, color,self.rect,
                        self.startAngle,self.stopAngle, self.lineWidth)
        end1 = (self.center[0]+self.radius*math.cos(self.stopAngle),
                self.center[1]-self.radius*math.sin(self.stopAngle))
        end2 = (self.center[0]+self.radius*math.cos(self.startAngle),
                self.center[1]-self.radius*math.sin(self.startAngle))
        pygame.draw.line(self.screen, color, self.center, end1, self.lineWidth)
        pygame.draw.line(self.screen, color, self.center, end2, self.lineWidth)



