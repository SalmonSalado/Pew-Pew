import pygame
from util import * 
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, max_vel, rotation_vel):
        super().__init__(group)

        self.import_assets() 

        self.pos = pos
        self.image = self.asset
        self.rect = self.image.get_rect(center=pos)

        # Keep the original rect and image to allow for rotation to be consistent

        self.img_original = self.image
        self.rect_original = self.rect

        self.max_vel = max_vel 
        self.vel = 0
        self.increament =  0.01
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.speed = 25 
        self.is_moving = False

    # Import the starting assets
    def import_assets(self):
        print('here')
        self.asset = pygame.transform.scale(pygame.image.load('../graphics/shooter.png').convert_alpha(), (32, 32))

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel

        if right:
            self.angle -= self.rotation_vel
    def move_forward(self, dt):
        if self.is_moving:
            self.vel = round(min( self.vel + self.speed * dt * self.increament, self.max_vel), 5) 
            self.move()
        else:
            self.reduce_speed(dt)
            self.move()
    def move(self):
        x = 0
        y = 0
        new_pos = self.pos

        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        x -= horizontal 
        y -= vertical
        new_pos = (self.pos[0] + x, self.pos[1] + y)
        self.pos = new_pos
        print(self.vel)
    # Function to reduce speed once the player stop pressing W
    def reduce_speed(self, dt):
        if not self.is_moving:
            self.vel = max(self.vel - (self.speed / 2) * dt * 0.025  , 0)
    # Function for inputs of the player
    def draw(self): 
        self.image , self.rect = rotate_img(self.img_original, self.pos, self.angle)

    def input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: 
            self.is_moving = True
            self.move_forward(dt)
        else:
            self.is_moving = False
            self.move_forward(dt)

        if keys[pygame.K_a]:
            self.rotate(left = True)
        if keys[pygame.K_d]:
            self.rotate(right = True) 
    def update(self, dt):
        self.draw()
        self.input(dt)
        self.rotate()
        self.move_forward(dt) 


class Example(pygame.sprite.Sprite):
    def __init__(self, pos, group,rotation_vel):
        super().__init__(group)

        self.image = pygame.Surface((50, 50))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        self.draw()

    def draw(self):
       self.image, self.rect.topleft = rotate_img(self.image,self.image.get_rect().topleft , 5)  

    def update(self, dt):
        self.draw()
