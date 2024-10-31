import pygame
from pygame._sdl2 import Window

from components import Sound
from engine import Engine
from screens.main_menu_screen import MainMenuScreen

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

Window.from_display_module().maximize()

pygame.display.set_caption("Nonogram")

engine = Engine(window)
engine.set_screen(MainMenuScreen(engine))
Sound.play_background_music()
engine.run(window, clock)

pygame.quit()
