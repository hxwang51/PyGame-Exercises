import sys
import random
import pygame
import math
from pygame.font import Font
from piece import Piece

def K_Index(index):
    '''根据 pieces 中 piece 对象的索引 index 返回对应的 pygame 键值'''
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
    '''在 screen 上画出 pieces 中的 piece 对象的序号
    screen: 将要画出序号的窗体
    index:  将要画出的序号
    centerx, centery: 饼图的圆心
    radius:           饼图的半径
    startAngle, stopAngle  每个 index 对应的 piece 对象的圆弧的起始弧度和结束弧度
    color:  用来画出序号的颜色
    '''
    font = Font(None, 30) # None 表示为 Pygame 默认字体，字号为 30 号
    fontTextImage = font.render(str(index), True, color)  # 把序号字符串渲染成图像
    # 确定序号在窗口上的位置: x, y 坐标
    fontTextPosition = (centerx + (radius / 2) * math.cos((startAngle + stopAngle) / 2),
                        centery - (radius / 2) * math.sin((startAngle + stopAngle) / 2))
    screen.blit(fontTextImage, fontTextPosition)

def get_start_stop_angles(index, numberPieces):
    '''根据 piece 对象的序号和饼图划分的块数
    确定 piece 上圆弧的起始弧度和结束弧度
    startAngle: 起始弧度
    stopAngle:  结束弧度
    '''
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
    done_color = (230, 0, 0)
    lineWidth=5

    numberPieces=9  # 取值范围为 1 到 9 ，因为最多只映射了 9 个数字按键
    pieces=[]
    drawPieces = [] # Boolean 数组，用于标记是否已经画出每个 piece
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
                        drawPieces[index]=True   # 按下一个数字键就标记对应的 piece 被画出
        screen.fill(bg_color)
        for index in range(numberPieces): # 画出序号
            startAngle, stopAngle = get_start_stop_angles(index, numberPieces)
            draw_index(screen, index+1, centerx, centery, radius, startAngle, stopAngle, pie_color)
        allDrawed = True # 标记是否所有 piece 都已经被画出
        for index in range(numberPieces):
            if drawPieces[index]:  # 实际画出被标记为 True 的 piece
                pieces[index].draw(pie_color)
            allDrawed = allDrawed and drawPieces[index]
        if allDrawed: # 如果所有 piece 都已经被画出
            for piece in pieces:
                piece.draw(done_color)
        pygame.display.update()

run_game()