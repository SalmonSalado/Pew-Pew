import pygame
from util import load_image

#button class
class Button:
    def __init__(self, pos, path_image, size):
        self.image = load_image(path_image, size) 
        self.rect = self.image.get_rect(center = pos)
        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        surface.blit(self.image, self.rect)
        
        return action
