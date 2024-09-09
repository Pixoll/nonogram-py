from typing import Self

import pygame
from pygame import Surface
from pygame.event import Event
from core.nonogram import Nonogram
from components.block import Block
from components.column import Column
from components.element import Element
from components.row import Row


class NonogramElement(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _horizontal_hints: tuple[tuple[Nonogram.Hint, ...], ...]
    _vertical_hints: tuple[tuple[Nonogram.Hint, ...], ...]

    def __init__(self, nonogram: Nonogram, size: int, padding: int):
        super().__init__(nonogram.size[0] * (size + padding) + padding, nonogram.size[1] * (size + padding) + padding)

        self._background_color = (192, 192, 192)
        self._padding = padding
        self._row = Row()
        self._horizontal_hints = nonogram.horizontal_hints
        self._vertical_hints = nonogram.vertical_hints
        for i in range(nonogram.size[0]):
            column = Column()
            for j in range(nonogram.size[1]):
                column.add_element(Block(size, size, nonogram[i, j]))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)

        self._surface = Surface((self.size[0] + padding * 2, self.size[1] + padding * 2), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(self.position)
        return self

    @property
    def size(self) -> tuple[int, int]:
        return self._row.size

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        return self

    def render(self, window: Surface):
        window.blit(self._surface, (self.position[0] - self._padding, self._position[1] - self._padding))
        self._row.render(window)

    def on_all_events(self, event: Event) -> None:
        for column_or_block in self._row.elements:
            if isinstance(column_or_block, Block):
                column_or_block.on_all_events(event)
            else:
                for block in column_or_block.elements:
                    block.on_all_events(event)
