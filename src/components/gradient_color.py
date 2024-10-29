from typing import Self

import pygame

from components.colored_block import ColoredBlock
from components.column import Column
from components.element import Element
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton


class GradientColor(Element):
    _surface: pygame.Surface
    _row: Row
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int]
    _block_size: int

    def __init__(self, color: tuple[int, int, int], block_size: int, padding: int) -> None:

        cols = 10  # Fixed 10 columns
        rows = 10  # Fixed 10 rows

        super().__init__(cols * (block_size + padding) - padding, rows * (block_size + padding) - padding)

        self._color = color
        self._block_size = block_size
        self._padding = padding
        self._background_color = (255, 255, 255)
        self._row = Row().set_alignment(VerticalAlignment.CENTER)
        self._selected_block = None
        self._selected_color = color

        aux2 = 1
        columns = []

        for i in range(10):
            aux1 = 1
            column = Column()
            for j in range(10):
                block = ColoredBlock(self._block_size, darken_color(self._color, aux1))
                if block.color == self._selected_color:
                    self._selected_block = block
                    block.change_state()
                column.add_element(block)
                aux1 += 1
            column.set_padding(self._padding)
            columns.append(column)
            self._color = lighten_color(self._color, aux2)
            aux2 += 1

        for column in reversed(columns):
            self._row.add_element(column)

        self._row.set_padding(self._padding)

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    def paint_gradient(self, color: tuple[int, int, int]) -> None:
        aux_row = Row().set_alignment(VerticalAlignment.CENTER)
        _color = color
        aux2 = 1
        columns = []
        self._selected_color = _color

        for i in range(10):
            aux1 = 1
            column = Column()
            for j in range(10):
                block = ColoredBlock(self._block_size, darken_color(_color, aux1))
                if block.color == self._selected_color:
                    self._selected_block = block
                    block.change_state()
                column.add_element(block)
                aux1 = aux1 + 1
            columns.append(column)
            column.set_padding(self._padding)
            _color = lighten_color(_color, aux2)
            aux2 = aux2 + 1

        for column in reversed(columns):
            aux_row.add_element(column)

        aux_row.set_padding(self._padding)
        self._row = aux_row
        self._row.set_position(self._position)

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row.elements:
            for block in column.elements:
                if block.contains(pygame.mouse.get_pos()):
                    # noinspection PyTypeChecker
                    b: ColoredBlock = block
                    color = b.color
                    self._selected_block.change_state()
                    self._selected_block = b
                    self._selected_color = color
                    b.change_state()

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._row.render(screen)

    def get_color(self) -> tuple[int, int, int]:
        return self._selected_color


def darken_color(color: tuple[int, int, int], level: int) -> tuple[int, int, int]:
    min_color_value = 0

    if level == 1:
        darken_factor = 0
    elif level < 5:
        darken_factor = (level / 10) * 0.6
    elif level <= 7:
        darken_factor = (level / 10) * 0.7
    else:
        darken_factor = (level / 10) * 0.8

    new_color = tuple(
        max(int(c - (c - min_color_value) * darken_factor), min_color_value) for c in color
    )
    if level == 10:
        new_color = (min_color_value, min_color_value, min_color_value)

    return new_color


def lighten_color(color: tuple[int, int, int], level: int) -> tuple[int, int, int]:
    lighten_factor = (level / 10) * 0.4

    return (
        min(color[0] + int((255 - color[0]) * lighten_factor), 255),
        min(color[1] + int((255 - color[1]) * lighten_factor), 255),
        min(color[2] + int((255 - color[2]) * lighten_factor), 255),
    )
