from typing import Self

import pygame

from components.colored_block import ColoredBlock
from components.column import Column
from components.element import Element
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton


class GradientColor(Element):
    _surface: pygame.Surface
    _row: Row[Column[ColoredBlock]]
    _padding: int
    _position: tuple[int, int]
    _block_size: int

    def __init__(self, color: tuple[int, int, int], block_size: int, padding: int) -> None:
        cols = 10
        rows = 10

        super().__init__(cols * (block_size + padding) - padding, rows * (block_size + padding) - padding)

        self._color = color
        self._block_size = block_size
        self._padding = padding
        self._row = Row().set_alignment(VerticalAlignment.CENTER)
        self._selected_block = None
        self._selected_color = color

        aux2 = 1
        columns: list[Column[ColoredBlock]] = []

        for i in range(cols):
            aux1 = 1
            column: Column[ColoredBlock] = Column()
            for j in range(rows):
                block = ColoredBlock(self._block_size, self._block_size, darken_color(self._color, aux1))
                if block.color == self._selected_color:
                    self._selected_block = block
                    block.toggle_selected()
                column.add_element(block)
                aux1 += 1
            column.set_padding(self._padding)
            columns.append(column)
            self._color = lighten_color(self._color, aux2)
            aux2 += 1

        self._selected_block.set_active(True)

        for column in reversed(columns):
            self._row.add_element(column)

        self._row.set_padding(self._padding)

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill((255, 255, 255, 128))

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    def set_active(self, active: bool) -> None:
        self._selected_block.set_active(active)

    def paint_gradient(self, color: tuple[int, int, int]) -> None:
        self._selected_color = color
        aux_color = color
        aux2 = 1

        for column in reversed(self._row):
            aux1 = 1
            for block in column:
                block.set_color(darken_color(aux_color, aux1))
                aux1 += 1

            aux_color = lighten_color(aux_color, aux2)
            aux2 += 1

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row:
            for block in column:
                if block.contains(pygame.mouse.get_pos()):
                    color = block.color
                    self._selected_block.toggle_selected()
                    self._selected_block = block
                    self._selected_color = color
                    block.toggle_selected()

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
