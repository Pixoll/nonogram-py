from typing import Self, Sequence

import pygame
from pygame import Surface

from assets import FontManager
from components.colored_block import ColoredBlock
from components.column import Column, HorizontalAlignment
from components.element import Element
from components.row import Row, VerticalAlignment
from core import Hint, Nonogram
from events import Event, EventType, MouseButton


class HintsElement(Element):
    _surface: Surface
    _padding: int
    _nonogram: Nonogram
    _hints: Sequence[Sequence[Hint]]
    _hint_elements: Column[Row[ColoredBlock]] | Row[Column[ColoredBlock]]

    def __init__(
            self,
            hints: Sequence[Sequence[Hint]],
            block_size: int,
            padding: int,
            is_horizontal: bool
    ):
        super().__init__(0, 0)
        self._hints = hints
        self._padding = padding
        hints_font = FontManager.get_default(int(block_size / 1.5))
        self._is_horizontal = is_horizontal
        self._hint_elements = Column() if is_horizontal else Row()
        self._grouped_blocks: dict[tuple[int, int, int], list[ColoredBlock]] = {}

        for i in range(len(hints)):
            row_or_column: Row[ColoredBlock] | Column[ColoredBlock] = Row() if is_horizontal else Column()

            for hint in hints[i]:
                hint_block = ColoredBlock(block_size, block_size, hint.color, str(hint.value), hints_font)

                if hint_block.color not in self._grouped_blocks:
                    self._grouped_blocks[hint_block.color] = [hint_block]
                else:
                    self._grouped_blocks[hint_block.color].append(hint_block)

                row_or_column.add_element(hint_block)

            row_or_column.set_padding(padding)
            self._hint_elements.add_element(row_or_column)
            self._hint_elements.set_alignment(
                HorizontalAlignment.RIGHT if self._is_horizontal
                else VerticalAlignment.BOTTOM
            )

        self._hint_elements.set_padding(padding)
        self._width, self._height = self._hint_elements.size

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._hint_elements.set_position(position)
        return self

    @property
    def hints(self) -> Sequence[Sequence[Hint]]:
        return self._hints

    @property
    def hint_elements(self) -> Sequence[Sequence[ColoredBlock]]:
        # noinspection PyTypeChecker
        return self._hint_elements

    def get_grouped_blocks(self, color: tuple[int, int, int]) -> Sequence[ColoredBlock]:
        return self._grouped_blocks[color]

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        self._hint_elements.render(window)
