from time import time

import pygame
from pygame import Surface
from pygame.font import Font

from components.column import Column, HorizontalAlignment
from components.container import Container
from components.row import Row, VerticalAlignment
from components.text import Text
from core import Nonogram
from events import Event, EventType, MouseButton


class NonogramInfoPreview(Container):
    _nonogram: Nonogram
    _size: Text
    _selected: bool

    def __init__(self, nonogram: Nonogram, width: int, height: int, font: Font) -> None:
        super().__init__(width, height, 25)
        self.set_background_color((0, 0, 0, 128))
        self.set_border((255, 255, 255, 128))
        self.set_border_width(int(width * 0.025))
        self._last_blink = 0

        self._nonogram = nonogram
        self._base = Column()

        size = f"{self._nonogram.size[0]}x{self._nonogram.size[1]}"
        self._size = Text(size, font, (255, 255, 255))

        row_of_size = Row()
        container_of_size = (Container(int(self._width * 0.9), int(self._height * 0.2))).set_child(self._size)
        row_of_size.add_element(container_of_size).set_alignment(VerticalAlignment.CENTER)

        row_of_name_or_state = Row()
        self._name = Text(nonogram.name, font, (255, 255, 255))
        container_of_name_or_state = Container(int(self._width * 0.9), int(self._height * 0.2))

        if nonogram.is_completed:
            container_of_name_or_state.set_child(self._name)
        elif nonogram.is_in_progress:
            container_of_name_or_state.set_child(Text("En progreso", font, (255, 255, 255)))
        else:
            container_of_name_or_state.set_child(Text("Incompleto", font, (255, 255, 255)))
        row_of_name_or_state.add_element(container_of_name_or_state).set_alignment(VerticalAlignment.CENTER)

        self._base.add_element(row_of_size).add_element(row_of_name_or_state).set_alignment(HorizontalAlignment.CENTER)

        self.set_child(self._base)

        self._selected = False

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
        self._size.render(window)
        pass
