import pygame, sys, time


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/Music/Music01.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def play_MenuClickSoundEffect():
    pygame.mixer.init()
    sound = pygame.mixer.Sound("assets\Music\MenuClickSound.mp3")
    sound.set_volume(0.3)
    sound.play()

def play_GameClickEffect():
    pygame.mixer.init()
    sound = pygame.mixer.Sound("assets\Music\ClickSound.mp3")
    sound.set_volume(0.3)
    sound.play()

