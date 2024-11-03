from typing import Self

import pygame
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.hints_element import HintsElement
from components.row import Row
from core import Nonogram
from events import Event, EventType, MouseButton


class NonogramElement(Element):
    _nonogram: Nonogram
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _grid: Row[Column[Block]]
    _grid_position: tuple[int, int]
    _block_size: int
    _horizontal_hints: HintsElement
    _vertical_hints: HintsElement
    _selected_color: tuple[int, int, int]

    def __init__(self, nonogram: Nonogram, block_size: int, padding: int):
        super().__init__(
            nonogram.size[0] * (block_size + padding) + padding,
            nonogram.size[1] * (block_size + padding) + padding
        )

        self._nonogram = nonogram
        self._background_color = (192, 192, 192)
        self._padding = padding
        self._grid = Row()
        self._grid_position = (0, 0)
        self._block_size = block_size
        self._horizontal_hints = HintsElement(nonogram.horizontal_hints, block_size, padding, True)
        self._vertical_hints = HintsElement(nonogram.vertical_hints, block_size, padding, False)
        self._selected_color = nonogram.used_colors[0]

        for i in range(nonogram.size[0]):
            column: Column[Block] = Column()
            for j in range(nonogram.size[1]):
                column.add_element(Block(block_size, block_size, nonogram[i, j]))
            self._grid.add_element(column)
            column.set_padding(padding)

        self._grid.set_padding(padding)

        self._width = self._horizontal_hints.size[0] + self._padding + self._grid.size[0]
        self._height = self._vertical_hints.size[1] + self._padding + self._grid.size[1]

        self._surface = Surface((self.size[0] + padding * 2, self.size[1] + padding * 2), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_zoom(self, zoom_factor: float) -> None:
        new_block_size = int(self._block_size * zoom_factor)
        self._block_size = new_block_size

        self._horizontal_hints.update_size(new_block_size)
        self._vertical_hints.update_size(new_block_size)

        for column in self._grid:
            column.set_element_sizes(new_block_size, new_block_size)

        self._width = self._horizontal_hints.size[0] + self._padding + self._grid.size[0]
        self._height = self._vertical_hints.size[1] + self._padding + self._grid.size[1]

        self.set_size(self._width, self._height)
        self._surface = Surface((self.size[0] + self._padding * 2, self.size[1] + self._padding * 2), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

        self.set_position(self._position)

    def set_position(self, position: tuple[int, int]) -> Self:

        self._position = position

        vertical_hint_position = (self._position[0] + self._horizontal_hints.size[0] + self._padding, self._position[1])
        horizontal_hint_position = (self._position[0], self._position[1] + self._vertical_hints.size[1] + self._padding)
        self._grid_position = (vertical_hint_position[0], horizontal_hint_position[1])

        self._vertical_hints.set_position(vertical_hint_position)
        self._horizontal_hints.set_position(horizontal_hint_position)
        self._grid.set_position(self._grid_position)

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

    def on_any_event(self, event: Event) -> None:

        if event.type == EventType.MOUSE_WHEEL:
            zoom_factor = 1.1 if event.y > 0 else 0.9
            self.set_zoom(zoom_factor)

        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        mouse_pos = pygame.mouse.get_pos()

        for column in self._grid:
            for block in column:
                if not block.contains(mouse_pos):
                    continue

                block.set_state(Block.State(int(event.button == MouseButton.LEFT)), self._selected_color)

                x = (mouse_pos[0] - self._grid_position[0]) // (self._block_size + self._padding)
                y = (mouse_pos[1] - self._grid_position[1]) // (self._block_size + self._padding)

                match block.state:
                    case Block.State.EMPTY:
                        self._nonogram[x, y] = None
                    case Block.State.CROSSED:
                        self._nonogram[x, y] = "x"
                    case Block.State.COLORED:
                        self._nonogram[x, y] = block.color
