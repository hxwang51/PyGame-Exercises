import pygame
import math
from pygame.font import Font

class Piece():
    '''这个类对饼图上的一小块进行抽象
    __init__() 函数的参数:
    screen:  主程序中由 pygame.display.set_mode() 创建的窗口对象
    centerx, centery  饼图的圆心坐标
                      ( screen 左上角的坐标为 (0, 0)，
                        并且 y 坐标向下增长，
                        x 坐标向右增长)
    radius: 饼图的半径
    startAngle, stopAngle Piece对象上的圆弧的起始和结束弧度数
    lineWidth: 所绘制的线条的宽度
    '''
    def __init__(self,
                 screen,
                 centerx, centery,
                 radius,
                 startAngle, stopAngle,
                 lineWidth):
        self.screen = screen
        self.center = centerx, centery   # 饼图的圆心 ( 坐标 )
        self.radius = radius
        self.rect = (self.center[0]-self.radius, self.center[1]-radius,  # 饼图外切矩形的左上角x, y 坐标
                     2*radius, 2*radius  # 饼图外切矩形的宽和高 width, height 当二者相等时绘制的是圆弧
                    )                    # 当二者不相等时，绘制的是椭圆弧
        self.startAngle = startAngle     # self.rect 的内切椭圆/圆上，圆心角为 startAngle 标记了圆弧的起始弧度
        self.stopAngle = stopAngle       # self.rect 的内切椭圆/圆上，圆心角为 stopAngle 标记了圆弧的结束弧度
        self.lineWidth = lineWidth

    def draw(self, color):
        # 画出 Piece 的圆弧弧线
        pygame.draw.arc(self.screen, color, self.rect,
                        self.startAngle,self.stopAngle, self.lineWidth)
        end1 = (self.center[0]+self.radius*math.cos(self.stopAngle),  # 圆弧的一个端点的坐标
                self.center[1]-self.radius*math.sin(self.stopAngle))
        end2 = (self.center[0]+self.radius*math.cos(self.startAngle), # 圆弧的另一个端点的坐标
                self.center[1]-self.radius*math.sin(self.startAngle))
        # 从圆心到这两个端点绘制直线
        pygame.draw.line(self.screen, color, self.center, end1, self.lineWidth)
        pygame.draw.line(self.screen, color, self.center, end2, self.lineWidth)
