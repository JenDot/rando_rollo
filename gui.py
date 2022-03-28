"""Pygame Frontend for Rando Rollo"""

from pickle import FALSE, TRUE
import sys, pygame
from turtle import width

# Define pygame tool variables
size = width, height = 500, 500
speed = [2,2]
screen = pygame.display.set_mode(size)
black = 0,0,0
wheel = pygame.image.load("raffle_wheel.svg")
wheelspot = wheel.get_rect()

class App:
    def __init__(self):
        pygame.init

        App.running = TRUE

def run(self):
    while App.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                App.running = FALSE
    wheelspot = pygame.transform.rotate(wheelspot,5)

    screen.fill(black)
    screen.blit(wheel, wheelspot)
    pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    App().run(host='192.168.122.31', port='5000', debug=True)