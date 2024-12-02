import pygame
from pygame import Surface
from pygame.font import Font

from assets import FontManager
from components.container import Container
from components.text import Text
from core import Nonogram
from events import Event, EventType, MouseButton
from components.row import VerticalAlignment, Row
from components.column import HorizontalAlignment, Column


# TODO should be implemented in nonograms_row.py
class NonogramInfoPreview(Container):
    _nonogram: Nonogram
    _size: Text
    _selected: bool

    def __init__(self, nonogram: Nonogram, width: int, height: int, font: Font) -> None:
        super().__init__(width, height)
        self._nonogram = nonogram
        self._background = Container(int(self._width*0.9), int(self._height*0.9)).set_background_color((37,218,147))
        self._base = Column()

        size = f"{self._nonogram.size[0]}x{self._nonogram.size[1]}"
        self._size = Text("Tamaño: "+size, FontManager.get_default(int(self._width * 0.1)), (99, 99, 224))

        row_of_size = Row()
        container_of_size = (Container(int(self._width * 0.9), int(self._height * 0.2))).set_child(self._size)
        row_of_size.add_element(container_of_size).set_alignment(VerticalAlignment.CENTER)

        row_of_name_or_state = Row()
        self._name = Text(nonogram.name, FontManager.get_default(height // 5), (99, 99, 224))
        container_of_name_or_state = Container(int(self._width * 0.9), int(self._height * 0.2))

        if nonogram.is_completed:
            container_of_name_or_state.set_child(self._name)
        else:
            container_of_name_or_state.set_child(Text("Estado: Incompleto", FontManager.get_default(int(self._width * 0.1)), (99, 99, 224)))
        row_of_name_or_state.add_element(container_of_name_or_state).set_alignment(VerticalAlignment.CENTER)

        self._base.add_element(row_of_size).add_element(row_of_name_or_state).set_alignment(HorizontalAlignment.CENTER)

        self._background.set_child(self._base)
        self.set_child(self._background)
        self.set_background_color((255, 255, 255))

        self.set_border((99, 99, 224))
        self.set_border_width(10)
        self._selected = False

    def set_selected(self, selected: bool) -> None:
        self._selected = selected
        new_color = (197, 194, 197) if selected else (255, 255, 255)
        self.set_background_color(new_color)

    def on_any_event(self, event: Event) -> None:
        super().on_any_event(event)
        pos = pygame.mouse.get_pos()
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            if super().contains(pos):
                self._selected = not self._selected
                new_color = (240, 20, 233) if self._selected else (255, 255, 255)
                self.set_background_color(new_color)

    def is_selected(self) -> bool:
        return self._selected

    def get_nonogram(self) -> Nonogram:
        return self._nonogram

    def render(self, window: Surface) -> None:
        super().render(window)
        self._size.render(window)
        pass

