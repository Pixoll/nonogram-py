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
    _background_color: tuple[int, int, int]
    _block_size: int
    _selected_color_index: int
    _selected_block: ColoredBlock
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
        self._background_color = (229, 229, 229)
        self._row = Row().set_alignment(VerticalAlignment.TOP)

        for i in range(cols):
            column: Column[ColoredBlock] = Column()
            for j in range(rows):
                index = i + j * cols
                if index < len(colors):
                    column.add_element(ColoredBlock(block_size, block_size, colors[index]))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)

        self._selected_color_index = 0
        self._selected_block = ColoredBlock(block_size, block_size, colors[self._selected_color_index]).set_position((
            self.position[0] + (self._row.size[0] - block_size) // 2,
            self.position[1] + self._row.size[1] + block_size
        ))

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        self._selected_block.set_position((
            self.position[0] + (self._row.size[0] - self._block_size) // 2,
            self.position[1] + self._row.size[1] + self._block_size
        ))
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
            self._selected_block.set_color(color)
            self._nonogram_element.set_selected_color(color)

        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row:
            for block in column:
                if block.contains(pygame.mouse.get_pos()):
                    block_color = block.color
                    self._selected_block.set_color(block_color)
                    self._nonogram_element.set_selected_color(block_color)

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._selected_block.render(screen)
        self._row.render(screen)
