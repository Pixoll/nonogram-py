from typing import Self

from pygame import Surface
from pygame.event import Event
from core.nonogram import Nonogram
from components.block import Block
from components.column import Column
from components.element import Element
from components.row import Row


class Board(Element):
    def __init__(self, nonogram: Nonogram, size: int, padding: int):
        super().__init__(*nonogram.size)

        self._row = Row()

        for i in range(nonogram.size[0]):
            column = Column()
            for j in range(nonogram.size[1]):
                column.add_element(Block(size, size, nonogram[i, j]).set_border_color((0, 0, 0, 64)))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(self.position)
        return self

    @property
    def size(self) -> tuple[int, int]:
        return self._row.size

    def render(self, window: Surface):
        self._row.render(window)

    def on_all_events(self, event: Event) -> None:
        for column_or_block in self._row.elements:
            if isinstance(column_or_block, Block):
                column_or_block.on_all_events(event)
            else:
                for block in column_or_block.elements:
                    block.on_all_events(event)
