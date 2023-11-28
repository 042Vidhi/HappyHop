
import pygame
from paths import ASSET_DIR
from utils.tools import sine
from config import ImageConfig

class VisualizationService:
    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSET_DIR / "Banana_cat.png").convert_alpha()
    
    @staticmethod
    def get_player_gameover_image():
        return pygame.image.load(ASSET_DIR / "Banana_cat_crying2.png").convert_alpha()
    
    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSET_DIR / "bg.png").convert_alpha()
    
    @staticmethod
    def get_title_image():
        return pygame.image.load(ASSET_DIR / "title.png").convert_alpha()
    
    @staticmethod
    def get_start_button_image():
        return pygame.image.load(ASSET_DIR / "start_button.png").convert_alpha()

    @staticmethod
    def get_banana_image():
        return pygame.image.load(ASSET_DIR / "Banana_Cat.png").convert_alpha()   
    
    @staticmethod
    def get_platform_image():
        return pygame.image.load(ASSET_DIR / "platform.png").convert_alpha()
    
    @staticmethod
    def get_obstacle1_image():
        return pygame.image.load(ASSET_DIR / "pot.png").convert_alpha()
    
    @staticmethod
    def get_obstacle2_image():
        return pygame.image.load(ASSET_DIR / "obstacle2.png").convert_alpha()

    @staticmethod
    def get_obstacle3_image():
        return pygame.image.load(ASSET_DIR / "obstacle2.png").convert_alpha()
    
    @staticmethod
    def draw_background_with_scroll(screen,scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (scroll,0))
        screen.blit(background, (ImageConfig.bg_width + scroll, 0))

    @staticmethod
    def load_main_game_display():
        pygame.display.set_caption("HappyHop")
        cat = VisualizationService.get_player_image()
        pygame.display.set_icon(cat)

    @staticmethod
    def draw_main_menu(screen):
        y = sine(200.0, 1280, 10.0, 40)
        
        title = pygame.image.load(ASSET_DIR / "title.png").convert_alpha()
        screen.blit(title, (250, y))
        
        press_start = pygame.image.load(ASSET_DIR / "start_button.png").convert_alpha()
        press_start_resized = pygame.transform.scale(press_start, (250,40))
        screen.blit(press_start_resized, (380, 200))
        
        banana_cat = VisualizationService.get_banana_image()
        banana_cat_resized = pygame.transform.scale(banana_cat, (250, 250))
        screen.blit(banana_cat_resized, (15, 70))

    @staticmethod
    def draw_game_over(screen):
        game_over = pygame.image.load(ASSET_DIR / "GameOver.png").convert_alpha()
        screen.blit(game_over, (220, 0))

        # press restart button
        press_restart = pygame.image.load(ASSET_DIR / "restart_button.png").convert_alpha()
        screen.blit(press_restart, (280, 100))


    @staticmethod
    def draw_score(screen, score):
        font = pygame.font.SysFont('comicsans', 25)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (50, 40))

