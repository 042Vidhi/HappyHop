

import pygame
import time
import sys

from global_state import GlobalState
from services.visualization_service import VisualizationService
from services.music_service import MusicService
from utils.tools import update_background_using_scroll, is_close_app_event
from components.game_status import GameStatus
from components.player import Player
from components.platform import Platform
from components.obstacles import Obstacle1
from components.score import Score
import random
from config import Config

GlobalState.load_screen()
VisualizationService.load_main_game_display()

P1 = Player()
Pf = Platform()
Sc = Score(0)

MAX_OBSTACLES = 3
ObstacleGroup = pygame.sprite.Group()



# ADDING INITIAL OBSTACLES
for i in range(MAX_OBSTACLES):
    x_position = random.randint(800,1600)
    y_position = Config.HEIGHT - 110
    new_obstacle = Obstacle1(x_position, y_position)
    ObstacleGroup.add(new_obstacle)


def main_menu_phase():

    for event in pygame.event.get():
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    VisualizationService.draw_main_menu(GlobalState.SCREEN)

    


def gameplay_phase():
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return
    # draw background
    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    
    # add player
    P1.draw(GlobalState.SCREEN)
    P1.update()
    Pf.draw(GlobalState.SCREEN,x=0,y=300)

    # add obstacles
    ObstacleGroup.update(GlobalState.SCROLL)
    ObstacleGroup.draw(GlobalState.SCREEN)

    if len(ObstacleGroup) < 4:
        x_position = random.randint(800,1600)
        y_position = Config.HEIGHT - 110
        new_obstacle = Obstacle1(x_position, y_position)
        ObstacleGroup.add(new_obstacle)

    for obstacle in ObstacleGroup:
        if P1.rect.right > obstacle.rect.left and not obstacle.passed:
            obstacle.passed = True
            MusicService.play_score_sound()
            Sc.add_score(1)

    VisualizationService.draw_score(GlobalState.SCREEN, Sc.score)
    # check collision
    # rectangular collision
    if pygame.sprite.spritecollide(P1, ObstacleGroup, False):
        # mask collision
        if pygame.sprite.spritecollide(P1, ObstacleGroup, False, pygame.sprite.collide_mask):
            MusicService.play_collsion_sound()
            GlobalState.GAME_STATE = GameStatus.GAME_OVER
            P1.image_index = 2

            # P1.draw(GlobalState.SCREEN)
            # P1.update() 
            game_over_phase()
            return



def game_over_phase():

    VisualizationService.draw_game_over(GlobalState.SCREEN)
    Sc.reset_score()
    for event in pygame.event.get():
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            reset_game()
            return

    # Add a slight delay to avoid processing multiple key presses
    pygame.time.delay(100)

    

def exit_game_phase():
    pygame.quit()
    sys.exit()

def reset_game():
    ObstacleGroup.empty()
    P1.rect.center = (50, 260)
    P1.game_over_flag = False
    P1.image_index = 0
