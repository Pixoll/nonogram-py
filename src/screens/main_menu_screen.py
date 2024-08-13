from pygame.event import Event

from src.engine import Engine
from src.screens.screen import Screen


class MainMenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

    def run_logic(self, event: Event) -> None:
        pass

    def render(self) -> None:
        pass
