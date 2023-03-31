import pygame as pg
import sys
from random import randint
from pygame.locals import *
WINDOW_SIZE = 600

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WINDOW_SIZE]*2)
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()







	
TicTacToe1337 = pygame.display.set_mode((600,600))
print(TicTacToe1337)
