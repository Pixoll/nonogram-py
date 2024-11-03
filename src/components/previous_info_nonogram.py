import pygame
from pygame import Surface

from assets import FontManager
from components.container import Container
from components.text import Text
from core.nonogram import Nonogram
from events import Event, EventType, MouseButton


# TODO should be implemented in row_of_nonograms.py
class PreviousInfoNonogram(Container):
    _nonogram: Nonogram
    _size: Text
    _selected: bool

    def __init__(self, nonogram: Nonogram, width: int, height: int) -> None:
        super().__init__(width, height)
        self._nonogram = nonogram
        size = f"{self._nonogram.size[0]}x{self._nonogram.size[1]}"
        self._size = Text(size, FontManager.get("sys", "Arial", 60), (99, 99, 224))
        self.set_child(self._size)
        self.set_background_color((255, 255, 255))
        self.set_border((99, 99, 224))
        self.set_border_width(10)
        self._selected = False

    def set_selected(self, selected: bool) -> None:
        self._selected = selected
        new_color = (197, 194, 197) if selected else (255, 255, 255)
        self.set_background_color(new_color)

    def on_any_event(self, event: Event) -> None:
        super().on_any_event(event)
        pos = pygame.mouse.get_pos()
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            if super().contains(pos):
                self._selected = not self._selected
                new_color = (197, 194, 197) if self._selected else (255, 255, 255)
                self.set_background_color(new_color)

    def is_selected(self) -> bool:
        return self._selected

    def get_nonogram(self) -> Nonogram:
        return self._nonogram

    def render(self, window: Surface) -> None:
        super().render(window)
        self._size.render(window)
        pass
