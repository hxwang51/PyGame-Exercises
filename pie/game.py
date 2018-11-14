import sys
import random
import pygame
import math
from pygame.font import Font
from piece import Piece

def K_Index(index):
    if index==0:
        return pygame.K_1
    elif index==1:
        return pygame.K_2
    elif index == 2:
        return pygame.K_3
    elif index == 2:
        return pygame.K_3
    elif index == 3:
        return pygame.K_4
    elif index == 4:
        return pygame.K_5
    elif index == 5:
        return pygame.K_6
    elif index == 6:
        return pygame.K_7
    elif index == 7:
        return pygame.K_8
    elif index == 8:
        return pygame.K_9

def draw_index(screen, index, centerx, centery, radius, startAngle, stopAngle, color):
    font = Font(None, 30)
    fontTextImage = font.render(str(index), True, color)
    fontTextPosition = (centerx + (radius / 2) * math.cos((startAngle + stopAngle) / 2),
                        centery - (radius / 2) * math.sin((startAngle + stopAngle) / 2))
    screen.blit(fontTextImage, fontTextPosition)

def get_start_stop_angles(index, numberPieces):
    startAngle = math.radians(index * (360 / numberPieces))
    stopAngle = math.radians((index + 1) * (360 / numberPieces))
    return startAngle, stopAngle

def run_game():
    pygame.init()
    window_size = 800, 600
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pie Game")
    centerx = 400
    centery = 300
    radius = 200
    pie_color = (200, 200, 0)
    bg_color = (0, 0, 200)
    lineWidth=5

    numberPieces=9
    pieces=[]
    drawPieces = []
    for index in range(numberPieces):
        startAngle, stopAngle = get_start_stop_angles(index, numberPieces)
        piece=Piece(screen, centerx, centery, radius, startAngle, stopAngle, lineWidth)
        pieces.append(piece)
        drawPieces.append(False)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for index in range(numberPieces):
                    if event.key == K_Index(index):
                        drawPieces[index]=True
        screen.fill(bg_color)
        for index in range(numberPieces):
            startAngle, stopAngle = get_start_stop_angles(index, numberPieces)
            draw_index(screen, index+1, centerx, centery, radius, startAngle, stopAngle, pie_color)
        allDrawed = True
        for index in range(numberPieces):
            if drawPieces[index]:
                pieces[index].draw(pie_color)
            allDrawed = allDrawed and drawPieces[index]
        if allDrawed:
            for piece in pieces:
                piece.draw((230, 0, 0))
        pygame.display.update()

run_game()