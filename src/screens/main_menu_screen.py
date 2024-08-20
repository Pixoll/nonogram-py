import pygame

from components import Container
from engine import Engine
from screens.screen import Screen
from events import Event, QuitEvent, KeyEvent


class MainMenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

        self.design = Container((1280, 720))
        self.design.set_color((0, 255, 255))
        self.design.alignment("center")

    def on_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.design.render(window)
