import pygame

from engine import Engine
from screens.main_menu_screen import MainMenuScreen
from components import Sound

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

pygame.display.set_caption("Nonogram")

engine = Engine(window)
engine.set_screen(MainMenuScreen(engine))
Sound.play_background_music()
engine.run(window, clock)

pygame.quit()
