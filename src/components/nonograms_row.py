from typing import Self

import pygame
from pygame.font import Font

from components.container import Container
from components.element import Element
from components.nonogram_info_preview import NonogramInfoPreview
from components.row import Row, VerticalAlignment
from components.text import Text
from core import Nonogram, nonogram_type_t, NonogramLoader, NonogramSize
from events import Event


class NonogramsRow(Element):
    def __init__(self, width: int, height: int, nonograms_type: nonogram_type_t, size: NonogramSize, font: Font):
        super().__init__(width, height)
        self._row: Row[NonogramInfoPreview] = Row().set_alignment(VerticalAlignment.CENTER)
        self._nonogram_entries = NonogramLoader.get_by_size(nonograms_type, size)
        self._font = font
        self._index = 0
        self._selected_nonogram = None

        self._nonograms_container: Container = Container(int(width * 0.7), height).set_child(self._row)

        self._elements = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(width * 0.05))

        arrow_size = int(height * 0.1)
        arrow_padding = arrow_size // 5

        self._left_arrow_double = (
            Container(arrow_size, arrow_size)
            .set_image("left_arrow_double.png", False)
            .fit_to_image()
        )
        self._left_arrow = (
            Container(arrow_size, arrow_size)
            .set_image("left_arrow.png", False)
            .fit_to_image()
        )

        self._elements.add_element(
            Row()
            .set_alignment(VerticalAlignment.CENTER)
            .set_padding(arrow_padding)
            .add_element(self._left_arrow_double)
            .add_element(self._left_arrow)
        )

        self._right_arrow = (
            Container(arrow_size, arrow_size)
            .set_image("right_arrow.png", False)
            .fit_to_image()
        )
        self._right_arrow_double = (
            Container(arrow_size, arrow_size)
            .set_image("right_arrow_double.png", False)
            .fit_to_image()
        )

        for i in range(4):
            entry = self._nonogram_entries[i]
            info_nonogram = NonogramInfoPreview(entry.load(), int(height * 0.4), int(height * 0.6))
            self._row.add_element(info_nonogram)

        self._elements.add_element(self._nonograms_container)
        self._elements.add_element(
            Row()
            .set_alignment(VerticalAlignment.CENTER)
            .set_padding(arrow_padding)
            .add_element(self._right_arrow)
            .add_element(self._right_arrow_double)
        )

        self._base: Container = Container(width, height).set_child(
            Container(int(width * 0.95), height).set_child(self._elements)
        )

        nothing_here_text = Text("Nothing here but us chickens", font, (0, 0, 0))

        self._nothing_here_but_us_chickens: Container = (
            Container(width, height)
            .set_child(
                Container(nothing_here_text.size[0] + int(width * 0.05), int(nothing_here_text.size[1] * 2.5), 25)
                .set_background_color((255, 255, 255, 128))
                .set_child(nothing_here_text)
            )
        )

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._base.set_position(position)
        self._nothing_here_but_us_chickens.set_position(position)
        return self

    def deselect(self) -> None:
        if self._selected_nonogram is not None:
            self._selected_nonogram.set_selected(False)
            self._selected_nonogram = None

    def get_selected_nonogram(self) -> Nonogram | None:
        if self._selected_nonogram is not None:
            return self._selected_nonogram.get_nonogram()
        return None

    def on_any_event(self, event: Event) -> None:
        for element in self._row:
            element.on_any_event(event)

            if element.is_selected():
                if self._selected_nonogram and self._selected_nonogram is not element:
                    self._selected_nonogram.set_selected(False)
                self._selected_nonogram = element

    def render(self, window: pygame.Surface) -> None:
        self._base.render(window)

        if len(self._row) == 0:
            self._nothing_here_but_us_chickens.render(window)
