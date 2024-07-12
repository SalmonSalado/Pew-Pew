import pygame
from entitie import *
from settings import * 
from button import Button
from util import *

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        # All groups that are gonna be used in the project
        self.all_game_sprites = CameraGroup()
        self.all_menu_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group() 


        # All the possible states of the game. Make sure that the names of the keys here match a function below
        # So that the algorithm is able to call it in the game state method.
        self.all_states = {

            'quit': False,
            'Pause_menu': False,
            'Main_menu': True,
            'Game_over': False,
            'Main_game': False 
        }

        self.setup()

    def setup(self):
        # Sets all the objects that we will be using in the project
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) , self.all_game_sprites,2,0.8, self.collision_sprites)
        self.bullet = Bullet((250, 250), self.all_game_sprites, self.player)
        self.meteors = Meteorites([self.all_game_sprites, self.collision_sprites],1500)
        self.menus = Menus()
        self.background_sprite = load_image('../graphics/background.png', (SCREEN_WIDTH, SCREEN_HEIGHT))

    def Game_over(self):
        # Resets the game to how it was at the start
        self.player.reset() 
        self.all_states['Game_over'] = False
        self.all_states['Main_menu'] = True
        # Removes all previously stated meteors so that they do not remain in the game.
        for meteor in self.meteors.list_meteors:
            meteor.kill()
        self.meteors = Meteorites([self.all_game_sprites, self.collision_sprites], 1500)
    # The start menu of the game
    def Main_menu(self):
        self.display_surf.blit(self.background_sprite, self.background_sprite.get_rect())
        if self.menus.main_menu(self.display_surf):
            self.all_states['Main_menu'] = False
            self.all_states['Main_game'] = True 

    def Main_game(self, dt):
        self.display_surf.fill((50,50,50))
        self.all_game_sprites.customize_draw(self.player)
        self.all_game_sprites.update(dt) 

    def Pause_menu(self):
        self.display_surf.fill((100, 100, 100))
        self.display_surf.blit(self.background_sprite, self.background_sprite.get_rect())
        if self.menus.pause(self.display_surf): 
            self.all_states['Main_game'] = True
            self.all_states['Pause_menu'] = False

    # Function that handles the decision of which state should the game be. 
    # Example: Should the game be in pause or continue just like that?
    def decide_state(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]: 
            self.all_states['Pause_menu'] = True
            self.all_states['Main_game'] = False 

        if self.player.game_over:
            self.all_states['Game_over'] = True
            self.all_states['Main_game'] = False

    # State of the game
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

        # iterates for every single sprite in the group
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surf.blit(sprite.image, offset_rect)
