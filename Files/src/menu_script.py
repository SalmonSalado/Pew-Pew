from settings import *
from util import load_image
from button import Button
# oethod for the menus in the game
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
