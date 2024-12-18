import pygame
# noinspection PyProtectedMember
from pygame._sdl2 import Window

from assets import SoundManager, TextureManager
from engine import Engine
from screens.main_menu_screen import MainMenuScreen

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720), flags=pygame.RESIZABLE)

Window.from_display_module().maximize()

pygame.display.set_icon(TextureManager.get("icon.png"))
pygame.display.set_caption("Nonogram")
SoundManager.play_music("music.mp3")

engine = Engine(window)
engine.set_screen(MainMenuScreen(engine))
engine.run(window, clock)

pygame.quit()
