import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

okno_sirka = 640
okno_vyska = 480

screen = pygame.display.set_mode((okno_sirka, okno_vyska), 0, 32)
pygame.display.set_caption("Pong Pong!")

# Creating 2 bars, a ball and background.
velikost_palky_x = 10
velikost_palky_y = int(input("Velikost palky (50 normalni hodnota): "))
velikost_micku = 15
back = pygame.Surface((okno_sirka, okno_vyska))
background = back.convert()
background.fill((0, 0, 0))
bar = pygame.Surface((velikost_palky_x, velikost_palky_y))
bar1 = bar.convert()
bar1.fill((0, 0, 255))
bar2 = bar.convert()
bar2.fill((255, 0, 0))
circ_sur = pygame.Surface((15, 15))
circ = pygame.draw.circle(circ_sur, (0, 255, 0), (velikost_micku / 2, velikost_micku / 2), velikost_micku / 2)
circle = circ_sur.convert()
circle.set_colorkey((0, 0, 0))

# some definitions
kolecko_rect_predchozi = [0,0]
kolecko_rect = [0,0]
bar1_x, bar2_x = 10., okno_sirka-20.
bar1_y, bar2_y = okno_vyska//2., okno_vyska//2.
circle_x, circle_y = okno_sirka//2., okno_vyska//2.
bar1_move, bar2_move = 0., 0.
speed_x = int(input("rychlost micku do stran (250 normalni hodnota): "))
speed_y = int(input("rychlost micku nahoru a dolu (250 normalni hodnota): "))
speed_circ = int(input("rychlost palek (250 normalni hodnota): "))
bar1_score, bar2_score = 0, 0
# clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

while True:
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.

    score1 = font.render(str(bar1_score), True, (255, 255, 255))
    score2 = font.render(str(bar2_score), True, (255, 255, 255))

    kolecko_rect_predchozi[0] = kolecko_rect[0]
    kolecko_rect_predchozi[1] = kolecko_rect[1]

    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(screen, (255, 255, 255), (330, 5), (330, 475))
    bar1_rect = screen.blit(bar1, (bar1_x, bar1_y))
    bar2_rect = screen.blit(bar2, (bar2_x, bar2_y))
    kolecko_rect = screen.blit(circle, (circle_x, circle_y))
    screen.blit(score1, (okno_sirka//3., okno_vyska//3.))
    screen.blit(score2, (float(okno_sirka*(3/4)), float(okno_vyska//3)))

    palky_rect = [0,0]
    palky_rect[0] = bar1_rect
    palky_rect[1] = bar2_rect

    bar1_y += bar1_move

    # movement of circle

    # AI of the computer.
    if circle_x >= okno_sirka//2.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5

    if bar1_y >= okno_vyska-velikost_palky_y:
        bar1_y = okno_vyska-velikost_palky_y-1
    elif bar1_y <= 0:
        bar1_y = 1
    if bar2_y >= okno_vyska-velikost_palky_y:
        bar2_y = okno_vyska-velikost_palky_y-1
    elif bar2_y <= 0:
        bar2_y = 1

    # since i don't know anything about collision, ball hitting bars goes like this.
    index_palky = kolecko_rect.collidelist(palky_rect)
    if index_palky > -1:
        speed_x = -speed_x          #otoci smer micku
        circle_x = kolecko_rect_predchozi[0]

    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y, bar_2_y = 215., 215.
    elif circle_x > okno_sirka-10.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.

    if circle_y <= 5.:
        speed_y = -speed_y
        #circle_y = 10.
    elif circle_y >= okno_vyska-15:
        speed_y = -speed_y
        #circle_y = okno_vyska-15

    pygame.display.update()