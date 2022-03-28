"""Pygame Frontend for Rando Rollo"""

import sys, pygame
from turtle import width
pygame.init()

size = width, height = 500, 500
speed = [2,2]
black = 0,0,0

screen = pygame.display.set_mode(size)

wheel = pygame.image.load("raffle_wheel.svg")
wheelspot = wheel.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    wheelspot = pygame.transform.rotate(wheelspot,5)

    screen.fill(black)
    screen.blit(wheel, wheelspot)
    pygame.display.flip()