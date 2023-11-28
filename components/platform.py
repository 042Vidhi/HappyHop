
import pygame
from services.visualization_service import VisualizationService

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_platform_image()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

