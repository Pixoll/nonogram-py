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
    _is_horizontal: bool

    def __init__(self, size: int, nonogram: Nonogram, padding: int, is_horizontal: bool):
        super().__init__(size, size)
        self._nonogram = nonogram
        self._padding = padding
        self._is_horizontal = is_horizontal
        hints_font = font.SysFont("Arial", int(size / 1.5))

        if self._is_horizontal:
            self._hints = nonogram.horizontal_hints
            self._colum_or_row = Column()
            for i in range(len(self._hints)):
                row = Row()

                for hint in self._hints[i]:
                    hint_block = ColoredBlock(size, hint.color, str(hint.value), hints_font)
                    row.add_element(hint_block)

                row.set_padding(padding)
                self._colum_or_row.add_element(row)
                self._colum_or_row.set_alignment(HorizontalAlignment.RIGHT)
            self._colum_or_row.set_padding(padding)
        else:
            self._hints = nonogram.vertical_hints
            self._colum_or_row = Row()

            for i in range(len(self._hints)):
                column = Column()

                for hint in self._hints[i]:
                    hint_block = ColoredBlock(size, hint.color, str(hint.value), hints_font)
                    column.add_element(hint_block)

                column.set_padding(padding)
                self._colum_or_row.add_element(column)
                self._colum_or_row.set_alignment(VerticalAlignment.BOTTOM)
            self._colum_or_row.set_padding(padding)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._colum_or_row.set_position(position)
        return self

    @property
    def hints(self) -> tuple[tuple[Nonogram.Hint, ...], ...]:
        return self._hints

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        self._colum_or_row.render(window)
