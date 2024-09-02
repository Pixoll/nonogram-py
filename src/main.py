import pygame

from engine import Engine
from screens.main_menu_screen import MainMenuScreen
from components.play_sounds import play_music

pygame.init()

# Reproduce la música de componente play_sounds
play_music()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

pygame.display.set_caption("Nonogram")

# Inicializa el Engine pasándole la ventana
engine = Engine(window)
engine.set_screen(MainMenuScreen(engine))
engine.run(window, clock)

pygame.quit()
