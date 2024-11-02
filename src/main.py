import pygame
from pygame._sdl2 import Window

from engine import Engine
from screens.create_screen import CreateScreen
from screens.main_menu_screen import MainMenuScreen
from screens.workshop_screen import WorkshopScreen

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

Window.from_display_module().maximize()

pygame.display.set_caption("Nonogram")

engine = Engine(window)
engine.set_screen(CreateScreen(engine))
engine.run(window, clock)

pygame.quit()
