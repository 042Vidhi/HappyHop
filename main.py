import pygame
import sys
from config import Config
from global_state import GlobalState
from components.game_status import GameStatus
from services.music_service import MusicService
from game_phases import main_menu_phase, gameplay_phase, exit_game_phase,game_over_phase

pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


# main function
def main():
    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_OVER:
            game_over_phase()

        MusicService.start_bg_music()
        update_game_display()

if __name__ == "__main__":
    main()
