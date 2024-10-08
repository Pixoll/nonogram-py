from typing import Self

from pygame import font, Surface

from components.colored_block import ColoredBlock
from components.column import Column, HorizontalAlignment
from components.element import Element
from components.row import Row, VerticalAlignment
from core.nonogram import Nonogram
from events import Event


class HintsElement(Element):
    _surface: Surface
    _padding: int
    _nonogram: Nonogram
    _hints: tuple[tuple[Nonogram.Hint, ...], ...]

    def __init__(
            self,
            hints: tuple[tuple[Nonogram.Hint, ...], ...],
            block_size: int,
            padding: int,
            is_horizontal: bool
    ):
        super().__init__(0, 0)
        self._hints = hints
        self._padding = padding
        hints_font = font.SysFont("Arial", int(block_size / 1.5))

        self._hint_elements = Column() if is_horizontal else Row()
        for i in range(len(hints)):
            row_or_column = Row() if is_horizontal else Column()

            for hint in hints[i]:
                hint_block = ColoredBlock(block_size, hint.color, str(hint.value), hints_font)
                row_or_column.add_element(hint_block)

            row_or_column.set_padding(padding)
            self._hint_elements.add_element(row_or_column)
            self._hint_elements.set_alignment(HorizontalAlignment.RIGHT if is_horizontal else VerticalAlignment.BOTTOM)

        self._hint_elements.set_padding(padding)
        self._width, self._height = self._hint_elements.size

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._hint_elements.set_position(position)
        return self

    @property
    def hints(self) -> tuple[tuple[Nonogram.Hint, ...], ...]:
        return self._hints

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        self._hint_elements.render(window)
