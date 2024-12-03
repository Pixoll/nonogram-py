from math import ceil
from typing import Self

import pygame
from pygame.font import Font

from components.colored_block import ColoredBlock
from components.column import Column
from components.container import Container
from components.nonogram_element import NonogramElement
from components.row import Row, VerticalAlignment
from components.text import Text
from events import Event, EventType, MouseButton, MouseWheelEvent


class ColorPicker(Container):
    _blocks: Row[Column[ColoredBlock]]
    _selected_color_index: int
    _nonogram_element: NonogramElement

    def __init__(
            self,
            nonogram_element: NonogramElement,
            colors: tuple[tuple[int, int, int], ...],
            block_size: int,
            font: Font
    ) -> None:
        cols = min(ceil(len(colors) ** 0.5), 5)
        rows = ceil(len(colors) / cols)
        width = cols * (block_size + 1) - 1
        height = rows * (block_size + 1) - 1

        colors_text = Text("Colors", font, (255, 255, 255))
        column_padding = colors_text.size[1] // 2

        super().__init__(
            max(width, colors_text.size[0]) + block_size,
            height + colors_text.size[1] + column_padding + block_size,
            25
        )
        self.set_background_color((0, 0, 0, 128))

        self._nonogram_element = nonogram_element
        self._colors = colors
        self._color_blocks = [ColoredBlock(block_size, block_size, colors[index]) for index in range(len(colors))]
        self._blocks = Row().set_alignment(VerticalAlignment.TOP).set_padding(1)

        for i in range(cols):
            column: Column[ColoredBlock] = Column().set_padding(1)
            for j in range(rows):
                index = i + j * cols
                if index < len(colors):
                    column.add_element(self._color_blocks[index])
            self._blocks.add_element(column)

        self._selected_color_index = 0
        self._selected_block = self._color_blocks[0]
        self._selected_block.toggle_selected()

        self.set_child(
            Container(self._width - block_size, self._height - block_size)
            .set_child(
                Column()
                .set_padding(column_padding)
                .add_element(colors_text)
                .add_element(self._blocks)
            )
        )

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

            self._selected_block.toggle_selected()
            self._selected_block = self._color_blocks[self._selected_color_index]
            self._selected_block.toggle_selected()

        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._blocks:
            for block in column:
                if block.contains(pygame.mouse.get_pos()):
                    self._selected_block.toggle_selected()
                    self._selected_block = block
                    block_color = block.color
                    block.toggle_selected()
                    self._nonogram_element.set_selected_color(block_color)
