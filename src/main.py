import pygame

from src.engine import Engine
from src.screens.main_menu_screen import MainMenuScreen

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

pygame.display.set_caption('Nonogram')

engine = Engine()
engine.set_screen(MainMenuScreen(engine))
engine.run(window, clock)

pygame.quit()
