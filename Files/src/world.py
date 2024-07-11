import pygame
from entitie import *
from settings import * 
from button import Button

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

        self.all_game_sprites = CameraGroup()
        self.all_menu_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()


        # All the possible states of the game. Make sure that the names of the keys here match a function below
        # So that the algorithm is able to call it in the game state method.
        self.all_states = {

            'quit': False,
            'Pause_menu': False,
            'Main_menu': False,
            'Game_over': False,
            'Main_game': True 
        }

        self.setup()

    def setup(self):
        # Sets all the objects that we will be using in the project
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) , self.all_game_sprites,2,0.8, self.collision_sprites)
        self.bullet = Bullet((250, 250), self.all_game_sprites, self.player)
        self.meteors = Meteorites([self.all_game_sprites, self.collision_sprites],1500)
        self.menus = Menus()

    def Game_over(self):
        pass

    def Main_menu(self):
        pass

    def Main_game(self, dt):
        self.display_surf.fill((50,50,50))
        self.all_game_sprites.customize_draw(self.player)
        self.all_game_sprites.update(dt) 

    def Pause_menu(self):
        self.display_surf.fill((180, 100, 200))
        if self.menus.pause(self.display_surf):
            print('paused')

    def decide_state(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]: 
            self.all_states['Pause_menu'] = True
            self.all_states['Main_game'] = False
        if keys[pygame.K_o]:
            self.all_states['Main_game'] = True
            self.all_states['Pause_menu'] = False

    def game_state(self, dt):
        self.decide_state() 

        # This gets all the function's name in all_states, checks if they are set to true in the dictionary
        # It also checks as well if the function is callable, A.K.A if it exist.
        # Additionally, we check if the main game is on so we can pass the dt ( delta time ) value to it
        for func_name, is_true in self.all_states.items():
            # check if the key's value is set to true
            if is_true:
                func = getattr(self, func_name, None)
                # Makes sure that the function is callable
                if callable(func):
                    if func == self.Main_game:
                        func(dt)
                    else:
                        func()
    def update(self, dt): 
        self.game_state(dt)

# Custom pygame.sprite.Group method that allows to have the illusion of a camera that follows the player
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.display_surf = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        # Determines the offset by which display all the rendered positions of the sprites, it doesn't affect their actual position
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2


        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surf.blit(sprite.image, offset_rect)
