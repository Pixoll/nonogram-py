from typing import Self

import pygame
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.hints_element import HintsElement
from components.row import Row
from core.nonogram import Nonogram
from events import Event, EventType, MouseButton


class NonogramElement(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _block_size: int
    _horizontal_hints: HintsElement
    _vertical_hints: HintsElement
    _selected_color: tuple[int, int, int]

    def __init__(self, nonogram: Nonogram, block_size: int, padding: int):
        super().__init__(
            nonogram.size[0] * (block_size + padding) + padding,
            nonogram.size[1] * (block_size + padding) + padding
        )

        self._background_color = (192, 192, 192)
        self._padding = padding
        self._grid = Row()
        self._block_size = block_size
        self._horizontal_hints = HintsElement(nonogram.horizontal_hints, block_size, padding, True)
        self._vertical_hints = HintsElement(nonogram.vertical_hints, block_size, padding, False)
        self._selected_color = nonogram.used_colors[0]

        for i in range(nonogram.size[0]):
            column = Column()
            for j in range(nonogram.size[1]):
                column.add_element(Block(block_size, block_size, nonogram[i, j]))
            self._grid.add_element(column)
            column.set_padding(padding)

        self._grid.set_padding(padding)

        self._width = self._horizontal_hints.size[0] + self._padding + self._grid.size[0]
        self._height = self._vertical_hints.size[1] + self._padding + self._grid.size[1]

        self._surface = Surface((self.size[0] + padding * 2, self.size[1] + padding * 2), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = (position[0] - self._horizontal_hints.size[0] // 2, position[1])
        vertical_hint_position = (self._position[0] + self._horizontal_hints.size[0] + self._padding, self._position[1])
        horizontal_hint_position = (self._position[0], self._position[1] + self._vertical_hints.size[1] + self._padding)

        self._vertical_hints.set_position(vertical_hint_position)
        self._horizontal_hints.set_position(horizontal_hint_position)
        self._grid.set_position((vertical_hint_position[0], horizontal_hint_position[1]))

        return self

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        return self

    def set_selected_color(self, color: tuple[int, int, int]) -> Self:
        self._selected_color = color
        return self

    def render(self, window: Surface):
        window.blit(self._surface, (self.position[0] - self._padding, self._position[1] - self._padding))
        self._vertical_hints.render(window)
        self._horizontal_hints.render(window)
        self._grid.render(window)

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        for column in self._grid.elements:
            for block in column.elements:
                # noinspection PyTypeChecker
                b: Block = block
                if b.contains(pygame.mouse.get_pos()):
                    b.set_state(Block.State(int(event.button == MouseButton.LEFT)), self._selected_color)
