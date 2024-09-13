from math import ceil
from typing import Self

import pygame

from components.color_block import ColorBlock
from components.column import Column
from components.element import Element
from components.nonogram_element import NonogramElement
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton


class ColorPicker(Element):
    _surface: pygame.Surface
    _row: Row
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int]
    _block_size: int
    _selected_block: ColorBlock
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
            column = Column()
            for j in range(rows):
                if i * rows + j < len(colors):
                    column.add_element(ColorBlock(block_size, colors[i * rows + j]))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)
        self.set_position((1000, 300))

        self._selected_block = ColorBlock(block_size, colors[0]).set_position((
            self.position[0] + (self._row.size[0] - block_size) // 2,
            self.position[1] + self._row.size[1] + block_size
        ))

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row.elements:
            for block in column.elements:
                if block.contains(pygame.mouse.get_pos()):
                    # noinspection PyTypeChecker
                    b: ColorBlock = block
                    color = b.color
                    self._selected_block.set_color(color)
                    self._nonogram_element.set_selected_color(color)

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._selected_block.render(screen)
        self._row.render(screen)
