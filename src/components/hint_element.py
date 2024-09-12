from typing import Self
from pygame import Surface
from sqlalchemy import column

from components.column import Column, HorizontalAlignment
from components.element import Element
from components.row import Row, VerticalAlignment
from components.color_block import ColorBlock
from core.nonogram import Nonogram
from events import Event

class HintElement(Element):
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

        if self._is_horizontal:
            self._hints = nonogram.horizontal_hints
            self._colum_or_row = Column()
            for i in range(len(self._hints)):
                row = Row()

                for hint in self._hints[i]:
                    hint_block = ColorBlock(size, size, hint.color,None)
                    hint_block.set_hint(hint.value)
                    row.add_element(hint_block)

                self._colum_or_row.add_element(row)
                self._colum_or_row.set_alignment(HorizontalAlignment.RIGHT)
        else:

            self._hints = nonogram.vertical_hints
            self._colum_or_row = Row()

            for i in range(len(self._hints)):
                column = Column()

                for hint in self._hints[i]:
                    hint_block = ColorBlock(size, size, hint.color, None)
                    hint_block.set_hint(hint.value)
                    column.add_element(hint_block)

                self._colum_or_row.add_element(column)
                self._colum_or_row.set_alignment(VerticalAlignment.BOTTOM)

    def set_position(self, position: tuple[int, int]) -> Self:
        pass

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        self._colum_or_row.render(window)
        pass
