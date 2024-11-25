from math import ceil
from typing import Self

import pygame

from components.colored_block import ColoredBlock
from components.column import Column
from components.element import Element
from components.nonogram_element import NonogramElement
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton, MouseWheelEvent


class ColorPicker(Element):
    _surface: pygame.Surface
    _row: Row[Column[ColoredBlock]]
    _padding: int
    _position: tuple[int, int]
    _block_size: int
    _selected_color_index: int
    _nonogram_element: NonogramElement

    def __init__(
            self,
            nonogram_element: NonogramElement,
            colors: tuple[tuple[int, int, int], ...],
            block_size: int,
            padding: int
    ) -> None:
        cols = min(ceil(len(colors) ** 0.5), 16)
        rows = ceil(len(colors) / cols)

        super().__init__(cols * (block_size + padding) - padding, rows * (block_size + padding) - padding)

        self._nonogram_element = nonogram_element
        self._colors = colors
        self._block_size = block_size
        self._padding = padding
        self._color_blocks = [ColoredBlock(block_size, block_size, colors[index]) for index in range(len(colors))]
        self._row = Row().set_alignment(VerticalAlignment.TOP).set_padding(padding)

        for i in range(cols):
            column: Column[ColoredBlock] = Column().set_padding(padding)
            for j in range(rows):
                index = i + j * cols
                if index < len(colors):
                    column.add_element(self._color_blocks[index])
            self._row.add_element(column)

        self._selected_color_index = 0
        self._selected_block = self._color_blocks[0]
        self._selected_block.change_state()

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill((0, 0, 0, 128))

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    def on_any_event(self, event: Event) -> None:
        if event.type == EventType.MOUSE_WHEEL:
            wheel_event: MouseWheelEvent = event
            down = wheel_event.precise_y < 0 if wheel_event.flipped else wheel_event.precise_y > 0

            self._selected_color_index += -1 if down else 1
            if self._selected_color_index >= len(self._colors):
                self._selected_color_index = 0
            elif self._selected_color_index < 0:
                self._selected_color_index = len(self._colors) - 1

            color = self._colors[self._selected_color_index]
            self._nonogram_element.set_selected_color(color)

            self._selected_block.change_state()
            self._selected_block = self._color_blocks[self._selected_color_index]
            self._selected_block.change_state()

        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row:
            for block in column:
                if block.contains(pygame.mouse.get_pos()):
                    self._selected_block.change_state()
                    self._selected_block = block
                    block_color = block.color
                    block.change_state()
                    self._nonogram_element.set_selected_color(block_color)

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._row.render(screen)
