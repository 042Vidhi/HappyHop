 
import pygame
from pygame.locals import *
from services.visualization_service import VisualizationService
from config import Config

vec = pygame.math.Vector2
RECT_COLOR = (0,255,255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        banana_cat = VisualizationService.get_player_image()
        banana_cat_resized = pygame.transform.scale(banana_cat, (100, 100))
        self.image = []
        self.image.append(banana_cat_resized)
        self.image.append(pygame.transform.flip(banana_cat_resized, True, False))
        # game_over_asset
        self.game_over_flag = False
        self.game_over_cat = VisualizationService.get_player_gameover_image()
        self.image.append(pygame.transform.scale(self.game_over_cat, (100, 100)))
        self.image_index = 0


        self.width = 55
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # initial position
        self.rect.center = (50, 260)
        # self.mask = pygame.mask.from_surface(self.image)
        # self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        
        

        # mask for collision detection
        self.mask = pygame.mask.from_surface(self.image[self.image_index])

    def draw(self, screen):
        screen.blit(self.image[self.image_index], (self.rect.x-22, self.rect.y-8))
        # pygame.draw.rect(screen,RECT_COLOR,self.rect,2)



    def update(self):

        key_pressed = pygame.key.get_pressed()

        # if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        #     self.rect.y -= 5
        # if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        #     self.rect.y += 5
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rect.x -= 5
            self.image_index = 1
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.rect.x += 5
            self.image_index = 0
        # jump
        if key_pressed[pygame.K_SPACE] or key_pressed[pygame.K_w]:
            self.vel.y = -10

        # # collision
        # if self.game_over_flag == True:
        #     self.image_index = 2
        #     self.game_over_flag = False

        # player should not go out of the screen
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > 800:
            self.rect.right = 800

        # gravity
        self.vel.y += Config.GRAVITY
        self.rect.y += self.vel.y

        # check if player is on the ground
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.vel.y = 0