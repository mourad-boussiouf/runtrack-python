import pygame as pg
import sys
from random import randint
from pygame.locals import *

WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE // 3

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.field_image = self.get_scaled_image(path='resources/field.png', res=[WINDOW_SIZE]*2)

    def draw(self, surface):
        surface.blit(self.field_image, (0, 0))

    @staticmethod
    def get_scaled_image(path, res):
        img=pg.image.load(path)
        return pg.transform.scale(img, res)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WINDOW_SIZE]*2)
        self.clock = pg.time.Clock()
        self.tictactoe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.screen.fill((255, 255, 255)) #b
            self.tictactoe.draw(self.screen,) #b
            pg.display.update()
            self.clock.tick(60)

if __name__=='__main__':
    game = Game()
    game.run()