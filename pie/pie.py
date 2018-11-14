import pygame
import math
from pygame.font import Font

class Pie():
    def __init__(self, index,
                 screen,
                 up_left_corner_x, up_left_corner_y,
                 length,
                 color,
                 start_angle, end_angle,
                 width):
        self.index = index
        self.screen = screen
        self.centerx, self.centery= up_left_corner_x+length/2, up_left_corner_y+length/2
        self.center = self.centerx, self.centery
        self.length = length
        self.end1 = (self.centerx+(float(length)/2)*math.cos(start_angle),
                     self.centery-(float(length)/2)*math.sin(start_angle))
        self.end2 = (self.centerx+(float(length)/2)*math.cos(end_angle),
                     self.centery-(float(length)/2)*math.sin(end_angle))
        self.rect = up_left_corner_x, up_left_corner_y, length, length
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.color = color
        self.width = width



    def draw(self):
        pygame.draw.arc(self.screen, self.color,self.rect,
                        self.start_angle,self.end_angle, self.width)
        pygame.draw.line(self.screen, self.color, self.center, self.end1, self.width)
        pygame.draw.line(self.screen, self.color, self.center, self.end2, self.width)
        self.draw_index()

    def draw_index(self):
        font = Font(None, 60)
        font_color = self.color
        fontTextImage = font.render(str(self.index), True, font_color)
        fontTextPosition = (self.centerx+(self.length/4)*math.cos((self.start_angle+self.end_angle)/2),
                            self.centery-(self.length/4)*math.sin((self.start_angle+self.end_angle)/2))
        self.screen.blit(fontTextImage, fontTextPosition)
