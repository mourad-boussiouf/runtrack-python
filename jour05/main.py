import pygame as pg
import sys
from random import randint
from pygame.locals import *
WINDOW_SIZE = 600

class Game:
    def __init__(self):
        pg.init()
        self.TicTacToe1337 = pg.display.set_mode([WINDOW_SIZE]*2)
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    def run(self):
        while True:
            self.check_events()
            self.clock.tick(60)
            pg.display.update()


if __name__=='__main__':
    game = Game()
    game.run()





