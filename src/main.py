import pygame

from src.engine import Engine
from src.screens.menu_screen import MenuScreen

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

pygame.display.set_caption('Nonogram')

engine = Engine()
engine.set_screen(MenuScreen(engine))
engine.run(window, clock)

pygame.quit()
