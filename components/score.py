
import pygame
class Score(pygame.sprite.Sprite):
    def __init__(self, score=0):
        self.score = score

    def add_score(self, score):
        self.score += score

    def get_score(self):
        return self.score
    
    def reset_score(self):
        self.score = 0

