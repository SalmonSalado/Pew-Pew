import pygame
from entitie import *
from settings import * 

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

        self.all_sprite = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) , self.all_sprite,10,0.05)
        # self.example = Example( (200, 200) , self.all_sprite,5)
        self.bullet = Bullet((250, 250), self.all_sprite, self.player)
        self.meteors = Meteorites(self.all_sprite, 500)
    def update(self, dt): 
        self.display_surf.fill((50,50,50))
        self.all_sprite.draw(self.display_surf)
        self.all_sprite.update(dt)
