from pygame.event import Event
import pygame

from src.components.container import Container
from src.components.text import Text
from src.engine import Engine
from src.screens.screen import Screen


class SettingsScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine
        self.menu = Container((1280, 720))
        self.menu.alignment("center")

        self.button1 = Container((200, 100))
        self.button1.set_color((207, 178, 171))
        self.button1.set_border((0, 0, 0))
        self.button1.set_child(Text("CTM", pygame.font.SysFont('Arial', 30),(0, 0, 0)))

        self.menu.set_child(self.button1)

    def run_logic(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.button1.position[0] <= mouse_pos[0] <= self.button1.position[0] + self.button1.width and \
                    self.button1.position[1] <= mouse_pos[1] <= self.button1.position[1] + self.button1.height:
                from src.screens.menu_screen import MenuScreen
                self.engine.set_screen(MenuScreen(self.engine))

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.menu.render(window)