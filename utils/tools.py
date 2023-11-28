import math

import pygame
from pygame.locals import *
from config import ImageConfig


def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return int(y)

def update_background_using_scroll(scroll):
    scroll -= 0.5

    if scroll < -ImageConfig.bg_width:
        scroll = 0

    return scroll



def is_close_app_event(event):
    return (event.type == QUIT) or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE)