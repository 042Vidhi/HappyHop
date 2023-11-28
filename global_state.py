import pygame
from components.game_status import GameStatus
from config import Config

class GlobalState:
    GAME_STATE = GameStatus.MAIN_MENU
    SCREEN = None
    SCROLL = 0

    @staticmethod
    def load_screen():
        screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        screen.fill((0, 255, 255))
        GlobalState.SCREEN = screen
        pygame.display.set_caption("HappyHop")
