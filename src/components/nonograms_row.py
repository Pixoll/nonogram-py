from typing import Self

import pygame
from pygame.font import Font

from components.container import Container
from components.element import Element
from components.nonogram_info_preview import NonogramInfoPreview
from components.row import Row, VerticalAlignment
from components.text import Text
from core import Nonogram, nonogram_type_t, NonogramLoader, NonogramSize
from events import Event, EventType, MouseButton


class NonogramsRow(Element):
    def __init__(
            self,
            width: int,
            height: int,
            nonograms_type: nonogram_type_t,
            size: NonogramSize,
            regular_font: Font,
            small_font: Font
    ):
        super().__init__(width, height)

        self._regular_font = regular_font
        self._small_font = small_font

        row_padding = int(width * 0.02)
        self._nonogram_previews: Row[NonogramInfoPreview] = (
            Row()
            .set_alignment(VerticalAlignment.CENTER)
            .set_padding(row_padding)
        )

        self._nonogram_entries = NonogramLoader.get_by_size(nonograms_type, size)
        self._index = 0
        self._previews_per_page = 3
        self._has_multiple_pages = len(self._nonogram_entries) > self._previews_per_page
        self._selected_nonogram: NonogramInfoPreview | None = None

        self._preview_width = int(width * 0.2)
        self._preview_height = self._preview_width * 4 // 3

        self._nonograms_container: Container = Container(
            (self._preview_width + row_padding) * self._previews_per_page - row_padding,
            height
        ).set_child(self._nonogram_previews)

        self._elements = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(width * 0.05))

        arrow_size = int(height * 0.1)
        arrow_padding = arrow_size // 3

        self._left_arrow_double = (
            Container(arrow_size, arrow_size)
            .set_image("left_arrow_double.png", False)
            .fit_to_image()
            .set_hidden(True)
        )
        self._left_arrow = (
            Container(arrow_size, arrow_size)
            .set_image("left_arrow.png", False)
            .fit_to_image()
            .set_hidden(True)
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
            .set_hidden(not self._has_multiple_pages)
        )
        self._right_arrow_double = (
            Container(arrow_size, arrow_size)
            .set_image("right_arrow_double.png", False)
            .fit_to_image()
            .set_hidden(not self._has_multiple_pages)
        )

        for i in range(min(self._previews_per_page, len(self._nonogram_entries))):
            entry = self._nonogram_entries[i]
            info_nonogram = NonogramInfoPreview(
                entry.load(),
                self._preview_width,
                self._preview_height,
                regular_font,
                small_font
            )
            self._nonogram_previews.add_element(info_nonogram)

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

        nothing_here_text = Text("Nothing here but us chickens", regular_font, (0, 0, 0))

        self._nothing_here_but_us_chickens: Container = (
            Container(width, height)
            .set_child(
                Container(nothing_here_text.size[0] + int(width * 0.05), int(nothing_here_text.size[1] * 2.5), 25)
                .set_background_color((255, 255, 255, 128))
                .set_child(nothing_here_text)
            )
        )

    @property
    def left_arrow(self) -> Container:
        return self._left_arrow

    @property
    def left_arrow_double(self) -> Container:
        return self._left_arrow_double

    @property
    def right_arrow(self) -> Container:
        return self._right_arrow

    @property
    def right_arrow_double(self) -> Container:
        return self._right_arrow_double

    @property
    def selected_nonogram(self) -> Nonogram | None:
        if self._selected_nonogram is not None:
            return self._selected_nonogram.get_nonogram()
        return None

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._base.set_position(position)
        self._nothing_here_but_us_chickens.set_position(position)
        return self

    def deselect(self) -> None:
        if self._selected_nonogram is not None:
            self._selected_nonogram.set_selected(False)
            self._selected_nonogram = None

    def on_any_event(self, event: Event) -> None:
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT and self._has_multiple_pages:
            mouse_pos = pygame.mouse.get_pos()

            if self._index > 0:
                clicked = False

                if not self._left_arrow.hidden and self._left_arrow.contains(mouse_pos):
                    self._index -= self._previews_per_page
                    clicked = True

                elif not self._left_arrow_double.hidden and self._left_arrow_double.contains(mouse_pos):
                    self._index -= self._previews_per_page * 2
                    self._index = max(self._index, 0)
                    clicked = True

                if clicked:
                    self._right_arrow.set_hidden(False)
                    self._right_arrow_double.set_hidden(False)
                    if self._index == 0:
                        self._left_arrow.set_hidden(True)
                        self._left_arrow_double.set_hidden(True)

                    for i in self._index_range:
                        self._replace_preview(i, i - self._index)

                    self._nonogram_previews.update_positions()
                    if self._selected_nonogram is not None:
                        self._selected_nonogram.set_selected(False)
                        self._selected_nonogram = None

                    return

            if self._index + self._previews_per_page < len(self._nonogram_entries):
                clicked = False

                if not self._right_arrow.hidden and self._right_arrow.contains(mouse_pos):
                    self._index += self._previews_per_page
                    clicked = True

                elif not self._right_arrow_double.hidden and self._right_arrow_double.contains(mouse_pos):
                    self._index += self._previews_per_page * 2
                    self._index = min(self._index, len(self._nonogram_entries) - self._previews_per_page)
                    clicked = True

                if clicked:
                    self._left_arrow.set_hidden(False)
                    self._left_arrow_double.set_hidden(False)
                    if self._index + self._previews_per_page >= len(self._nonogram_entries):
                        self._right_arrow.set_hidden(True)
                        self._right_arrow_double.set_hidden(True)

                    for i in self._index_range:
                        self._replace_preview(i, i - self._index)

                    self._nonogram_previews.update_positions()
                    if self._selected_nonogram is not None:
                        self._selected_nonogram.set_selected(False)
                        self._selected_nonogram = None

                    return

        for i in range(min(self._previews_per_page, len(self._nonogram_entries))):
            nonogram_preview = self._nonogram_previews[i]
            nonogram_preview.on_any_event(event)

            if nonogram_preview.is_selected():
                if self._selected_nonogram and self._selected_nonogram is not nonogram_preview:
                    self._selected_nonogram.set_selected(False)
                self._selected_nonogram = nonogram_preview

    def render(self, window: pygame.Surface) -> None:
        self._base.render(window)

        if len(self._nonogram_entries) == 0:
            self._nothing_here_but_us_chickens.render(window)

    @property
    def _index_range(self) -> range:
        return range(self._index, max(self._index + self._previews_per_page, len(self._nonogram_previews)))

    def _replace_preview(self, entry_index: int, preview_index: int) -> None:
        entry = self._nonogram_entries[entry_index]
        info_nonogram = NonogramInfoPreview(
            entry.load(),
            self._preview_width,
            self._preview_height,
            self._regular_font,
            self._small_font
        )
        self._nonogram_previews[preview_index] = info_nonogram
