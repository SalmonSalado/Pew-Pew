import pygame
import sys
from world import Level

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def running(self):
        run = True

        while run:
            #self.screen.fill('BLACK')            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        run = False
                        sys.exit()
            dt = self.clock.tick() / 1000
            pygame.display.update()
            self.level.update(dt)

if __name__ == '__main__':
    game = Game()
    game.running()
