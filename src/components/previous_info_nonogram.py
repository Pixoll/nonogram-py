from typing import Self

import pygame
from pygame import Surface

from components import Element, Text, Container
from core.nonogram import Nonogram
from events import Event


# TODO should be implemented in row_of_nonograms.py
class PreviousInfoNonogram(Container):
    _nonogram: Nonogram
    _size: Text

    def __init__(self, nonogram: Nonogram, width: int, height: int) -> None:
        super().__init__(width, height)
        self._nonogram = nonogram
        size = f"{self._nonogram.size[0]}x{self._nonogram.size[1]}"
        self._size = Text(size, pygame.font.SysFont("Arial", 60), (99, 99, 224))
        self.set_child(self._size)
        self.set_background_color((255, 255, 255))
        self.set_border((99, 99, 224))
        self._border_width = 10


    def set_position(self, position: tuple[int, int]) -> Self:
        super().set_position(position)
        pass

    def on_any_event(self, event: Event) -> None:
        super().on_any_event(event)
        pass

    def render(self, window: Surface) -> None:
        super().render(window)
        self._size.render(window)
        pass
