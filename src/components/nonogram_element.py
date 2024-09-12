from typing import Self

import pygame
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.hint_element import HintElement
from components.row import Row
from core.nonogram import Nonogram
from events import Event, EventType, MouseButton


class NonogramElement(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _horizontal_hints: HintElement
    _vertical_hints: HintElement
    _selected_color: tuple[int, int, int]

    def __init__(self, nonogram: Nonogram, size: int, padding: int):
        super().__init__(nonogram.size[0] * (size + padding) + padding, nonogram.size[1] * (size + padding) + padding)

        self._background_color = (192, 192, 192)
        self._padding = padding
        self._row = Row()
        self._horizontal_hints = HintElement(size,nonogram, padding,True)
        self._vertical_hints = HintElement(size,nonogram, padding,False)
        self._selected_color = nonogram.used_colors[0]

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
        max_horizontal_hint_blocks = max(len(hints) for hints in self._horizontal_hints._hints)
        max_vertical_hint_blocks = max(len(hints) for hints in self._vertical_hints._hints)

        block_size = self._horizontal_hints.size[0]

        vertical_hint_position = (
        self._position[0], self._position[1] - max_vertical_hint_blocks *  (self._padding + block_size))

        horizontal_hint_position = (
        self._position[0] - max_horizontal_hint_blocks * (self._padding + block_size), self._position[1])

        self._vertical_hints.set_position(vertical_hint_position)
        self._horizontal_hints.set_position(horizontal_hint_position)

        self._row.set_position(self._position)

        return self

    @property
    def size(self) -> tuple[int, int]:
        return self._row.size

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

        self._row.render(window)

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        for column in self._row.elements:
            for block in column.elements:
                # noinspection PyTypeChecker
                b: Block = block
                if b.contains(pygame.mouse.get_pos()):
                    b.set_state(Block.State(int(event.button == MouseButton.LEFT)), self._selected_color)
