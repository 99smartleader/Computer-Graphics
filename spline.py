# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:22:18 2022
@author: 99smartleader/smartwolf99
"""

import pygame

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
class Position:
    def __init__(self, x, y, text = " "):
        self.x = x
        self.y = y
        self.text = text
    def display(self, screen, color):
        text = font.render(self.text, True, color)
        textRect = text.get_rect()
        if self.y > 540:
            textRect.center = (self.x , self.y + 30)
        else:
            textRect.center = (self.x , self.y - 35)

        screen.blit(text, textRect)
        pygame.draw.circle(screen, color, (self.x, self.y), 12)
        pygame.draw.circle(screen, (120, 120, 120), (self.x, self.y), 10)

def LinearCurve(positions, t, screen, color, trigger=True):
    P0_x = (1 - t) * positions[0].x
    P0_y = (1 - t) * positions[0].y

    P1_x = t * positions[1].x
    P1_y = t * positions[1].y

    curve = (P0_x + P1_x, P0_y + P1_y)
    
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, color, (positions[0].x, positions[0].y),(int(curve[0]), int(curve[1])), 5)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    elif trigger == False:
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
        return (int(curve[0]), int(curve[1]))

def QuadraticCurve(positions, t, screen, color, curve_list, green, trigger= True):

    P0_x = pow((1-t), 2) * positions[0].x
    P0_y = pow((1-t), 2) * positions[0].y

    P1_x = 2 * (1-t) * t * positions[1].x
    P1_y = 2 * (1-t) * t * positions[1].y

    P2_x = t ** 2 * positions[2].x
    P2_y = t ** 2 * positions[2].y

    curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
        first_line = [positions[0], positions[1]]
        second_line = [positions[1], positions[2]]

        a = LinearCurve(first_line, t,  screen, green, False)
        b = LinearCurve(second_line, t,  screen, green, False)

        pygame.draw.line(screen, green, a, b, 2)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))

def CubicCurve(positions, t, screen, color, curve_list, green, blue, quad_curve, quad_curve1, quad_curve2):
    P0_x = pow((1 - t), 3) * positions[0].x
    P0_y = pow((1 - t), 3) * positions[0].y

    P1_x = 3 * pow((1-t), 2) * t * positions[1].x
    P1_y = 3 * pow((1-t), 2) * t * positions[1].y

    P2_x = 3 * (1-t) * pow(t, 2) * positions[2].x
    P2_y = 3 * (1-t) * pow(t, 2) * positions[2].y

    P3_x = pow(t, 3) * positions[3].x
    P3_y = pow(t, 3) * positions[3].y

    curve = (P0_x + P1_x + P2_x + P3_x, P0_y + P1_y + P2_y + P3_y)

    pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
    pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
    pygame.draw.line(screen, (0, 0, 0), (positions[2].x, positions[2].y), (positions[3].x, positions[3].y), 1)

    first_line = [positions[0], positions[1]]
    second_line = [positions[1], positions[2]]
    third_line = [positions[2], positions[3]]
    fourth_line = [positions[0], positions[1], positions[2]]
    fifth_line = [positions[1], positions[2], positions[3]]
    sixth_line = [positions[0], positions[2], positions[3]]

    a = LinearCurve(first_line, t,  screen, green, False)
    b = LinearCurve(second_line, t,  screen, green, False)
    c = LinearCurve(third_line, t,  screen, green, False)

    pygame.draw.line(screen, green, a, b, 2)
    pygame.draw.line(screen, green, b, c, 2)

    QuadraticCurve(fourth_line, t, screen, (100, 100, 0), quad_curve, green)
    QuadraticCurve(fifth_line, t, screen, (100, 100, 0), quad_curve1, green)
    QuadraticCurve(sixth_line, t, screen, (100, 100, 0), quad_curve2, green, False)

    position_1 = Position(a[0], a[1])
    position_2 = Position(b[0], b[1])
    position_3 = Position(c[0], c[1])

    line1 = [position_1, position_2]
    line2 = [position_2, position_3]

    start = LinearCurve(line1, t, screen, blue, False)
    end = LinearCurve(line2, t, screen, blue, False)

    pygame.draw.line(screen, blue, start, end, 2)

    pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))
    

#from positions import Position
#from curves import *

width, height = 1920, 1080
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 32)

#colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)
blue = (2, 146, 242)
purple = (205, 163, 255)

#parameters
t = 0
speed = 0.002
linear_positions = [Position(100, 800, "P0"), Position(300, 200, "P1")]
Quadratic_positions = [Position(660, 800, "P0"), Position(880, 450, "P1"), Position(720, 200, "P2")]
cubic_positions = [Position(1050, 800, "P0"), Position(1280, 200, "P1"), Position(1420, 800, "P2"), Position(1800, 200, "P3")]

quadratic_curve = []
cubic_curve = []
curve1 = []
curve2 = []
curve3 = []

run = True
while run:
    screen.fill(white)
    clock.tick(fps)
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Bezier Curve - FPS : {}".format(frameRate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    # Gui Text
    text = font.render(" T = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (960, 100)
    screen.blit(text, textRect)
    linear = font.render("Linear " , True, black)
    
    textRect = linear.get_rect()
    textRect.center = (240, 120)
    screen.blit(linear, textRect)
    Quadratic = font.render("Quadratic", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (620, 120)
    screen.blit(Quadratic, textRect)

    cubic = font.render("Cubic", True, black)
    textRect = cubic.get_rect()
    textRect.center = (1400, 120)
    screen.blit(cubic, textRect)

    #separator ---- | ----- | ------
    pygame.draw.line(screen, purple, (480, 850), (480, 150), 1)
    pygame.draw.line(screen, purple, (950, 850), (950, 150), 1)

    LinearCurve(linear_positions, t, screen, red)
    QuadraticCurve(Quadratic_positions, t, screen, red, quadratic_curve, green)
    CubicCurve(cubic_positions, t, screen, red, cubic_curve, green, blue, curve1, curve2, curve3)

    if len(cubic_curve) > 2:
        pygame.draw.lines(screen, (179, 179, 179),False,  curve1, 3)
        pygame.draw.lines(screen, (179, 179, 179),False,  curve3, 3)
        pygame.draw.lines(screen, (179, 179, 179),False,  curve2, 3)
        pygame.draw.lines(screen, red,False,  cubic_curve, 5)

    if len(quadratic_curve) > 2:
        pygame.draw.lines(screen, red,False,  quadratic_curve, 5)

    if t >= 1:
        t = 0
        quadratic_curve.clear()
        cubic_curve.clear()
        curve1.clear()
        curve2.clear()
        curve3.clear()

    # draw points
    for point in linear_positions:
        point.display(screen, black)
    for point in Quadratic_positions:
        point.display(screen, black)
    for point in cubic_positions:
        point.display(screen, black)

    t += speed
    pygame.display.update()

pygame.quit()
