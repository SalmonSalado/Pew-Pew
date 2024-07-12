import pygame
from button import Button
import random
from util import * 
import math
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, max_vel, rotation_vel, collision_sprites):
        super().__init__(group)
       # Gets all the sprites that are collideable. 
        self.collision_sprites = collision_sprites
        # Imports the assets for the class
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
        self.speed = 10
        self.is_moving = False 

        # To check if the game should end
        self.game_over = False

    # Import the starting assets
    def import_assets(self): 
        self.asset = load_image('../graphics/shooter.png', (32, 32)) 

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
    # Method that move the player and calculates how much should the player move based on the angle that its facing
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
        # print(self.vel)
    # Function to reduce speed once the player stop pressing W
    def reduce_speed(self, dt):
        if not self.is_moving:
            self.vel = max(self.vel - (self.speed / 2) * dt * 0.025  , 0) 
    
    # Function that check if a collision occured with the player.rect and if that's so, then create a mask of the object and the player
    # To provide pixel perfect collision.
    # This way, the program avoids creating a mask every single time
    # And instead only creates it when a collision has ocurred and it has to make sure
    # that it is an overlap between the two sprites and not just their pygame.rect
    def collision_check(self): 
        for sprite in self.collision_sprites.sprites(): 
            if sprite.rect.colliderect(self.rect): 
                sprite_mask = pygame.mask.from_surface(sprite.image)
                player_mask = pygame.mask.from_surface(self.image)
                if sprite_mask.overlap(player_mask , (self.rect.x - sprite.rect.x , self.rect.y - sprite.rect.y)):
                    self.game_over = True 


    # Function used to reset the player once the game is over
    def reset(self):
        self.game_over = False
        self.pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = 0
        self.rect.center = self.pos
        self.angle = 0

    def draw(self): 
        self.image , self.rect = rotate_img(self.img_original, self.pos, self.angle)

    # Method that handles all the inputs of the player
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
        self.collision_check()

# Class for the meteor that appears in the game
class Meteor(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group) 

        self.pos = pos

        self.image = None
        self.load_asset()
        self.rect = self.image.get_rect(center = self.pos)

    def load_asset(self):
        self.image = load_image('../graphics/meteor.png' , (64,64)) 

# Class that handles all the meteors in the game
class Meteorites:
    def __init__(self,group, amount):
        self.list_meteors = []

        for meteor in range(amount):
            meteor = Meteor((random.randint(0, 10000) , random.randint(0, 10000)) , group) 
            self.list_meteors.append(meteor) 
        # print(self.list_meteors)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, group, player):
        super().__init__(group)
        self.player = player
        self.pos = pos
        
        self.image = None
        self.load_asset() 
        self.rect = self.image.get_rect(center = pos)

    def load_asset(self):
        self.image = load_image('../graphics/bullet.png' , (32,32))

    def move(self):
        pass

    def delete_self(self):
        pass

    def update(self, dt):
        pass
# Method for the menus in the game
class Menus:
    def __init__(self):
        # The Button class provides a method that allows to check if the user has pressed the button with the mouse
        # It is checked using the Button.draw() method
        self.paused_button = Button((SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2) , '../graphics/paused_button0.png' , (96, 64)) 
        self.play_button = Button((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), '../graphics/play_button0.png', (94, 64))

    def pause(self, surface): 
        if self.paused_button.draw(surface):
            self.paused_button.image = load_image('../graphics/paused_button1.png', (96, 64))
            return True
        else: 
            return False
    def main_menu(self, surface):
        if self.play_button.draw(surface):
            self.play_button.image = load_image('../graphics/play_button1.png', (94, 64))
            return True
        else:
            return False

# Something to be used for tests
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
