
import pygame
from paths import MUSIC_DIR

class MusicService:
    @staticmethod
    def play_collsion_sound():
        collision_sound = pygame.mixer.Sound(MUSIC_DIR / "collision.wav")
        pygame.mixer.Sound.play(collision_sound)

    @staticmethod
    def play_score_sound():
        score_sound = pygame.mixer.Sound(MUSIC_DIR / "score.wav")
        pygame.mixer.Sound.play(score_sound)

    @staticmethod
    def start_bg_music():
        if pygame.mixer.music.get_busy():
            return
        
        pygame.mixer.music.load(MUSIC_DIR / "bg.mp3")
        pygame.mixer.music.play()