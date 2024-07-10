import pygame
from entitie import *
from settings import * 

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

        self.all_sprite = CameraGroup()

        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) , self.all_sprite,2,0.3)
        self.bullet = Bullet((250, 250), self.all_sprite, self.player)
        self.meteors = Meteorites(self.all_sprite,1500)
    def update(self, dt): 
        self.display_surf.fill((50,50,50))
        self.all_sprite.customize_draw(self.player)
        self.all_sprite.update(dt)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.display_surf = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2


        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surf.blit(sprite.image, offset_rect)
