import sys
import os
import pygame
import math
from pie import Pie

def run_game():
    pygame.init()
    window_size = 800, 600
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pie Game")
    centerx = 400
    centery = 300
    length = 300
    pie_color = (200, 200, 0)
    bg_color = (0, 0, 200)
    width=5
    pie1=Pie(1, screen, centerx-length/2, centery-length/2,
             length, pie_color,
             math.radians(0), math.radians(90),
             width)
    pie2=Pie(2, screen, centerx-length/2, centery-length/2,
             length, pie_color,
             math.radians(90), math.radians(180),
             width)
    pie3=Pie(3, screen, centerx-length/2, centery-length/2,
             length, pie_color,
             math.radians(180), math.radians(270),
             width)
    pie4=Pie(4, screen, centerx-length/2, centery-length/2,
             length, pie_color,
             math.radians(270), math.radians(360),
             width)

    drawPie1=False
    drawPie2=False
    drawPie3=False
    drawPie4=False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    drawPie1=True
                elif event.key == pygame.K_2:
                    drawPie2=True
                elif event.key == pygame.K_3:
                    drawPie3=True
                elif event.key == pygame.K_4:
                    drawPie4=True
        screen.fill(bg_color)
        if drawPie1:
            pie1.draw()
        if drawPie2:
            pie2.draw()
        if drawPie3:
            pie3.draw()
        if drawPie4:
            pie4.draw()
        if drawPie1 and drawPie2 and drawPie3 and drawPie4:
            pie1.color=pie2.color=pie3.color=pie4.color=(255, 0, 0)
            pie1.draw()
            pie2.draw()
            pie3.draw()
            pie4.draw()
            font=pygame.font.Font(None, 60)
            fontTextImage=font.render("You Win!", True, (255,255,255))
            fontTextRect=fontTextImage.get_rect()
            screen.blit(fontTextImage, (centerx-fontTextRect.width/2,
                                        centery-fontTextRect.height/2))
        pygame.display.update()

run_game()