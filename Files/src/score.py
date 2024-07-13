import pygame

class Score:
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score

        self.font = pygame.font.Font(None , 32)
        self.score_text = self.font.render(f"Score: {self.score}" , True, (255,255,255))

    def draw(self, surface):
        self.score_text = self.font.render(f"Score: {self.score}" , True, (255,255,255))
        surface.blit(self.score_text , self.pos)

    def update(self, player, surface):
        self.score = player.coin_score
        self.draw(surface)
