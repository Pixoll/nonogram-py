import pygame

from components import Container, Text
from engine import Engine
from screens.screen import Screen
from events import Event, QuitEvent, KeyEvent


class SettingsScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine
        self.menu = Container((1280, 720))
        self.menu.alignment("center")

        self.button1 = Container((200, 100))
        self.button1.set_color((207, 178, 171))
        self.button1.set_border((0, 0, 0))
        self.button1.set_child(Text("CTM", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        self.menu.set_child(self.button1)

    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.button1.position[0] <= mouse_pos[0] <= self.button1.position[0] + self.button1.width and \
                    self.button1.position[1] <= mouse_pos[1] <= self.button1.position[1] + self.button1.height:
                from screens.main_menu_screen import MainMenuScreen
                self.engine.set_screen(MainMenuScreen(self.engine))

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.menu.render(window)
