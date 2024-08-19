from pygame.event import Event
import pygame

from src.components.column import Column
from src.components.container import Container
from src.components.text import Text
from src.components.row import Row
from src.engine import Engine
from src.screens.screen import Screen


class MainMenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

        self.design = Container((1280, 720))
        self.design.set_color((0, 255, 255))
        self.design.alignment("center")


    def run_logic(self, event: Event) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.design.render(window)