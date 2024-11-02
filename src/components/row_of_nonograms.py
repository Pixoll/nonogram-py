from typing import Self

import pygame

from components.element import Element
from components.previous_info_nonogram import PreviousInfoNonogram
from components.row import Row, VerticalAlignment
from components.scroll_bar import ScrollBar
from core.nonogram import Nonogram
from events import Event


class RowOfNonograms(Element):
    _row: Row
    _list_of_nonograms: list[Nonogram]
    _scrollbar: ScrollBar
    _selected_nonogram: PreviousInfoNonogram | None = None

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._row = Row()
        self._list_of_nonograms = []

        for i in range(1, 100):
            nonogram = Nonogram.from_pre_made(i)
            self._list_of_nonograms.append(nonogram)

            size_index_str = f"{nonogram.size[0]}x{nonogram.size[1]}"
            info_nonogram = PreviousInfoNonogram(nonogram, self._width * 0.8, self._height)
            self._row.add_element(info_nonogram)
        content_width = len(self._list_of_nonograms) * info_nonogram.size[0]
        self._scrollbar = ScrollBar(width, content_width)

        self._row.set_alignment(VerticalAlignment.CENTER)

    def get_selected_nonogram(self) -> Nonogram | None:
        if self._selected_nonogram:
            return self._selected_nonogram.get_nonogram()
        return None

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        self._scrollbar.set_position((position[0], position[1] + self._height - 20))
        return self

    @property
    def nonograms(self) -> list[Nonogram]:
        return self._list_of_nonograms

    def on_any_event(self, event: Event) -> None:
        self._scrollbar.on_any_event(event)

        for element in self._row:
            if isinstance(element, PreviousInfoNonogram):
                element.on_any_event(event)

                if element.is_selected():
                    if self._selected_nonogram and self._selected_nonogram is not element:
                        self._selected_nonogram.set_selected(False)
                    self._selected_nonogram = element

    def update(self):
        self._scrollbar.update()
        scroll_offset = self._scrollbar.x_axis
        self._row.set_position((self._position[0] + scroll_offset, self._position[1]))

    def render(self, window: pygame.Surface) -> None:
        self.update()
        self._row.render(window)
        self._scrollbar.render(window)
