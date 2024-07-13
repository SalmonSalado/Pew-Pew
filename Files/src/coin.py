import pygame
from settings import *
from util import load_image
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.pos = pos

        self.image = None
        self.load_asset()
        self.rect = self.image.get_rect(center=pos)

        # Variable for checking if the sprite is a coin
        self.is_coin = True

        # To check whether to delete or not
        self.delete_this = False

    def load_asset(self):
        self.image = load_image('../graphics/coin.png' , (32,32))


class Coins:
    def __init__(self, group , amount):
        self.list_coins = [] 

        for coin in range(amount): 
            bounds_x = [random.randint(-LIMIT_DISTANCE , SCREEN_WIDTH - 200) , random.randint(SCREEN_WIDTH + 200, LIMIT_DISTANCE)]
            bounds_y = [random.randint(-LIMIT_DISTANCE , SCREEN_HEIGHT - 200) , random.randint(SCREEN_HEIGHT + 200 ,  LIMIT_DISTANCE)]
            coin = Coin( (random.choice(bounds_x) , random.choice(bounds_y)), group )
            self.list_coins.append(coin) 

    def update(self):
        for coin in self.list_coins:
            if coin.delete_this:
                coin.kill()
