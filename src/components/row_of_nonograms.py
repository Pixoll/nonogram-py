from components import Element, Row, Text, Container, VerticalAlignment
from components.scroll_bar import ScrollBar
from core.nonogram import Nonogram
import pygame
from events import Event
from typing import Self


class RowOfNonograms(Element):
    _row: Row
    _list_of_nonograms: list[Nonogram]
    _scrollbar: ScrollBar

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._row = Row()
        self._list_of_nonograms = []

        for i in range(1, 100):
            nonogram = Nonogram.from_pre_made(i)
            self._list_of_nonograms.append(nonogram)

            size_index_str = f"{nonogram.size[0]}x{nonogram.size[1]}"
            print(size_index_str)

            info_nonogram = (
                Container(int(self._width * 0.6), int(self._height * 0.6))
                .set_background_color((255, 255, 255))
                .set_border((255, 255, 255))
                .set_child(
                    Text(
                        size_index_str,
                        pygame.font.SysFont("Arial", 80),
                        (99, 99, 224)
                    )
                    .set_color((152, 99, 224))
                )
            )
            self._row.add_element(info_nonogram)
        content_width = len(self._list_of_nonograms) * 200
        print(content_width,len(self._list_of_nonograms))
        self._scrollbar = ScrollBar(width, content_width)

        self._row.set_alignment(VerticalAlignment.CENTER)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        self._scrollbar.set_position((position[0], position[1] + self._height - 20))
        return self

    @property
    def nonograms(self) -> list[Nonogram]:
        return self._list_of_nonograms

    def on_all_events(self, event: Event) -> None:
        self._scrollbar.on_all_events(event)
        for element in self._row.elements:
            element.on_all_events(event)

    def update(self):
        self._scrollbar.update()
        scroll_offset = self._scrollbar.x_axis
        self._row.set_position((self._position[0] + scroll_offset, self._position[1]))

    def render(self, window: pygame.Surface) -> None:
        self.update()
        self._row.render(window)
        self._scrollbar.render(window)


