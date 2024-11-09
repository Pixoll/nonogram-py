from typing import Self

import pygame

from components.element import Element
from components.previous_info_nonogram import PreviousInfoNonogram
from components.row import Row, VerticalAlignment
from components.scroll_bar import ScrollBar
from core import Nonogram, nonogram_type_t, NonogramLoader
from events import Event


class RowOfNonograms(Element):
    _row: Row[PreviousInfoNonogram]
    _list_of_nonograms: list[Nonogram]
    _scrollbar: ScrollBar | None
    _selected_nonogram: PreviousInfoNonogram | None = None

    def __init__(self, width: int, height: int, nonograms_type: nonogram_type_t):
        super().__init__(width, height)
        self._row = Row()
        self._list_of_nonograms = []

        for i in range(1, 101):
            try:
                nonogram = NonogramLoader.load(nonograms_type, i)
            except ValueError:
                break

            self._list_of_nonograms.append(nonogram)

            info_nonogram = PreviousInfoNonogram(nonogram, self._height, self._height)
            self._row.add_element(info_nonogram)

        if len(self._list_of_nonograms) == 0:
            self._scrollbar = None
            return

        content_width = len(self._list_of_nonograms) * self._height
        self._scrollbar = ScrollBar(width, content_width)

        self._row.set_alignment(VerticalAlignment.CENTER)

    def deselect(self) -> None:
        if self._selected_nonogram is not None:
            self._selected_nonogram.set_selected(False)
            self._selected_nonogram = None

    def get_selected_nonogram(self) -> Nonogram | None:
        if self._selected_nonogram is not None:
            return self._selected_nonogram.get_nonogram()
        return None

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        if self._scrollbar is not None:
            self._scrollbar.set_position((position[0], position[1] + self._height - 20))
        return self

    def on_any_event(self, event: Event) -> None:
        if self._scrollbar is not None:
            self._scrollbar.on_any_event(event)

        for element in self._row:
            element.on_any_event(event)

            if element.is_selected():
                if self._selected_nonogram and self._selected_nonogram is not element:
                    self._selected_nonogram.set_selected(False)
                self._selected_nonogram = element

    def update(self):
        if self._scrollbar is not None:
            self._scrollbar.update()
            scroll_offset = self._scrollbar.x_axis
            self._row.set_position((self._position[0] + scroll_offset, self._position[1]))

    def render(self, window: pygame.Surface) -> None:
        self.update()
        self._row.render(window)
        if self._scrollbar is not None:
            self._scrollbar.render(window)
