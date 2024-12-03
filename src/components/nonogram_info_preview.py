from time import time
from typing import Self

import pygame
from pygame import Surface
from pygame.font import Font

from components.column import Column, HorizontalAlignment
from components.container import Container
from components.text import Text
from core import Nonogram
from events import Event, EventType, MouseButton


class NonogramInfoPreview(Container):
    _nonogram: Nonogram
    _size_text: Text
    _selected: bool

    def __init__(self, nonogram: Nonogram, width: int, height: int, regular_font: Font, small_font: Font) -> None:
        super().__init__(width, height, 25)
        self.set_background_color((0, 0, 0, 128))
        self.set_border((255, 255, 255, 128))
        self.set_border_width(int(width * 0.025))

        self._last_blink = 0
        self._nonogram = nonogram
        self._selected = False

        self._id_text = Text(f"id: {nonogram.id}", small_font, (255, 255, 255))
        self._id_text.set_position((
            self.position[0] + (width - self._id_text.size[0]) // 2,
            self.position[1] + height - self._id_text.size[1] * 2
        ))

        max_text_width = int(width * 0.85)
        nonogram_name: str = (nonogram.name if nonogram.is_completed
                              else "".join("?" if c != " " else " " for c in nonogram.name)).strip()

        nonogram_name_container = Column()

        last_space = 0
        for i in range(len(nonogram_name)):
            name_slice = nonogram_name[last_space:i + 1]
            if regular_font.size(name_slice)[0] < max_text_width:
                if i + 1 == len(nonogram_name):
                    nonogram_name_container.add_element(Text(name_slice, regular_font, (255, 255, 255)))
                continue

            first_space = i
            for l in range(i, last_space - 1, -1):
                if name_slice[l] == " ":
                    first_space = l
                    break

            if first_space > last_space:
                name_slice = nonogram_name[last_space:first_space]
                last_space = first_space + 1
            else:
                name_slice = name_slice[last_space:i] + "-"
                last_space = i

            nonogram_name_container.add_element(Text(name_slice, regular_font, (255, 255, 255)))

            if i + 1 == len(nonogram_name) and len(last_slice := nonogram_name[last_space:i + 1]) > 0:
                nonogram_name_container.add_element(Text(last_slice, regular_font, (255, 255, 255)))

        self.set_child(
            Column()
            .set_alignment(HorizontalAlignment.CENTER)
            .set_padding(int(width * 0.1))
            .add_element(Text(
                f"{self._nonogram.size[0]}x{self._nonogram.size[1]}",
                regular_font,
                (255, 255, 255)
            ))
            .add_element(nonogram_name_container)
            .add_element(Text(
                "Completed" if nonogram.is_completed
                else "In progress" if nonogram.is_in_progress
                else "Not played",
                regular_font,
                (255, 255, 255)
            ))
        )

    def set_position(self, position: tuple[int, int]) -> Self:
        super().set_position(position)
        self._id_text.set_position((
            self.position[0] + (self._width - self._id_text.size[0]) // 2,
            self.position[1] + self._height - self._id_text.size[1] * 2
        ))
        return self

    def set_selected(self, selected: bool) -> None:
        self._selected = selected
        self._last_blink = 0
        self.set_border((255, 255, 255, 128))

    def on_any_event(self, event: Event) -> None:
        super().on_any_event(event)
        pos = pygame.mouse.get_pos()
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            if super().contains(pos):
                self.set_selected(True)

    def is_selected(self) -> bool:
        return self._selected

    def get_nonogram(self) -> Nonogram:
        return self._nonogram

    def render(self, window: Surface) -> None:
        if self._selected and (now := time()) - self._last_blink > 0.5:
            self._last_blink = now
            self.set_border(
                (236, 36, 138, 128) if self._border_color == (255, 255, 255, 128) else (255, 255, 255, 128)
            )

        super().render(window)
        self._id_text.render(window)
