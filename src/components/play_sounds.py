import pygame, sys, time


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/Music/Music01.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
