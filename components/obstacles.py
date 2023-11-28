
import pygame
import random
from services.visualization_service import VisualizationService

class Obstacle1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rand_img_no = random.randint(1,3)
        if self.rand_img_no == 1:
            self.image = VisualizationService.get_obstacle1_image()
        elif self.rand_img_no == 2:
            self.image = VisualizationService.get_obstacle2_image()
        else:
            self.image = VisualizationService.get_obstacle3_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.passed = False

        # mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,scroll):
        self.rect.x -= 6
        if self.rect.right < 0:
            self.kill()
        
    