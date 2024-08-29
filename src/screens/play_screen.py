from pygame.event import Event
import pygame

from components.container import Container
from components.board import Board
from components.nonogram_element import NonogramElement
from core.nonogram import Nonogram
from engine import Engine
from screens.screen import Screen
from events import Event, EventType, KeyEvent, QuitEvent, MouseButton

class PlayScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine, nonograma:Nonogram):
        self.engine = engine
        self.menu = Container((1280, 720))
        self.menu.alignment("center")
        self.board = NonogramElement(nonograma)

        self.menu.set_child(self.board)

    def on_event(self, event: Event) -> None:
        self.board.run_logic(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.menu.render(window)