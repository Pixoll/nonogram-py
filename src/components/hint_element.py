from typing import Self
from pygame import Surface
from components.column import Column
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
    _vertical: bool

    def __init__(self, size: int, nonogram: Nonogram, padding: int, vertical: bool):
        super().__init__(size, size)
        self._nonogram = nonogram
        self._padding = padding
        self._vertical = vertical

        if self._vertical:
            self._hints = nonogram.vertical_hints
            self._colum_or_row = Column()
            for i in range(len(self._hints)):
                for hint in self._hints[i]:
                    hint_block = ColorBlock(size, size, (200, 200, 200))
                    hint_block.set_hint(hint)
                    self._colum_or_row.add_element(hint_block)
        else:
            self._hints = nonogram.horizontal_hints
            self._colum_or_row = Row()
            for i in range(len(self._hints)):
                for hint in self._hints[i]:
                    hint_block = ColorBlock(size, size, (200, 200, 200))
                    hint_block.set_hint(hint)
                    self._colum_or_row.add_element(hint_block)
    def set_position(self, position: tuple[int, int]) -> Self:
        pass

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        self._colum_or_row.render(window)
        pass
