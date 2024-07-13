import pygame

class SoundManager:
    def __init__(self):
        self.song = pygame.mixer.Sound('../sound/main_music.mp3')
        self.song.play(-1)
