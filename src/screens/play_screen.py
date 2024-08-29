import pygame

from components import ChildAlignment, Container, NonogramElement
from core.nonogram import Nonogram
from engine import Engine
from events import Event, KeyEvent, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class PlayScreen(Screen):
    _engine: Engine
    _menu: Container
    _nonogram: NonogramElement

    def __init__(self, engine: Engine, nonogram: Nonogram):
        self._engine = engine
        self._menu = Container(1280, 720).set_child_alignment(ChildAlignment.CENTER)
        self._nonogram = NonogramElement(nonogram)
        self._menu.set_child(self._nonogram.board)

    def on_all_events(self, event: Event) -> None:
        self._nonogram.board.on_all_events(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        pass

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._menu.render(window)
