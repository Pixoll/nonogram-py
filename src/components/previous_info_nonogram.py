from typing import Self

import pygame
from pygame import Surface

from components import Element, Text
from core.nonogram import Nonogram
from events import Event


# TODO should be implemented in row_of_nonograms.py
class PreviousInfoNonogram(Element):
    _nonogram: Nonogram
    _size: Text

    def __init__(self, nonogram: Nonogram, ) -> None:
        super().__init__(nonogram.size[0] * 25, nonogram.size[1] * 25)
        self.nonogram = nonogram
        size = f"{nonogram.size[0]}x{nonogram.size[1]}"
        self._size = (Text(size, pygame.font.SysFont("Arial", 60), (99, 99, 224))
                      .set_position((self.size[0], self.size[1] // 4)))

    def set_position(self, position: tuple[int, int]) -> Self:
        pass

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        pass
