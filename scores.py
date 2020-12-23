import pygame

class Score():
    def __init__(self, score = 0):
        self.amount = score

    def update(self, sprite_group1, sprite_group2, score, multiplier = 0):
        pygame.sprite.spritecollideany(sprite_group1, sprite_group2).kill()
        self.amount += max(1, multiplier) * score