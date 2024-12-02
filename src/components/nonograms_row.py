from typing import Self, Sequence

import pygame
from pygame.font import Font

from components.container import Container
from components.element import Element
from components.nonogram_info_preview import NonogramInfoPreview
from components.row import Row, VerticalAlignment
from components.text import Text
from core import Entry, Nonogram, nonogram_type_t, NonogramLoader, NonogramSize
from events import Event


class NonogramsRow(Element):
    _row: Row[NonogramInfoPreview]
    _nonogram_entries: Sequence[Entry]
    _selected_nonogram: NonogramInfoPreview | None = None

    def __init__(self, width: int, height: int, nonograms_type: nonogram_type_t, size: NonogramSize, font: Font):
        super().__init__(width, height)
        self._row = Row().set_alignment(VerticalAlignment.CENTER)
        self._nonogram_entries = NonogramLoader.get_by_size(nonograms_type, size)
        self._font = font
        self._index = 0

        for i in range(5):
            entry = self._nonogram_entries[i]
            nonogram = NonogramLoader.load(nonograms_type, entry.nonogram_id)
            info_nonogram = NonogramInfoPreview(nonogram, int(height * 0.3), int(height * 0.3))
            self._row.add_element(info_nonogram)

        self._base = Container(width, height).set_child(self._row)

        nothing_here_text = Text("Nothing here but us chickens", font, (0, 0, 0))

        self._nothing_here_but_us_chickens: Container = (
            Container(width, height)
            .set_child(
                Container(nothing_here_text.size[0] + int(width * 0.05), int(nothing_here_text.size[1] * 2.5), 25)
                .set_background_color((255, 255, 255, 128))
                .set_child(nothing_here_text)
            )
        )

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
        self._base.set_position(position)
        self._nothing_here_but_us_chickens.set_position(position)
        return self

    def on_any_event(self, event: Event) -> None:
        for element in self._row:
            element.on_any_event(event)

            if element.is_selected():
                if self._selected_nonogram and self._selected_nonogram is not element:
                    self._selected_nonogram.set_selected(False)
                self._selected_nonogram = element

    def render(self, window: pygame.Surface) -> None:
        self._row.render(window)

        if len(self._row) == 0:
            self._nothing_here_but_us_chickens.render(window)
