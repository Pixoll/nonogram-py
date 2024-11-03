from enum import auto, Enum
from typing import Self, TypeVar

from components.element import Element
from components.element_bundle import ElementBundle
from events import Event


class VerticalAlignment(Enum):
    TOP = auto()
    CENTER = auto()
    BOTTOM = auto()


T = TypeVar("T", bound=Element)


class Row(ElementBundle[T]):
    _alignment: VerticalAlignment
    _max_height: int

    def __init__(self):
        super().__init__()
        self._alignment = VerticalAlignment.CENTER
        self._max_height = 0

    def set_alignment(self, alignment: VerticalAlignment) -> Self:
        self._alignment = alignment
        self._update_positions()
        return self

    def on_any_event(self, event: Event) -> None:
        pass

    def set_element_sizes(self, width: int, height: int) -> Self:
        for element in self._elements:
            element.set_size(width, height)
        self._update_size()
        self._update_positions()

        return self
    def _update_size(self) -> None:
        if not self._elements:
            self._width = 0
            self._height = 0
            return

        self._width = sum(element._width for element in self._elements) + self._padding * (len(self._elements) - 1)
        self._height = max(element._height for element in self._elements)
        self._max_height = self._height

    def _update_positions(self) -> None:
        x_offset = 0

        for element in self._elements:
            y_offset = 0

            match self._alignment:
                case VerticalAlignment.TOP:
                    y_offset = 0
                case VerticalAlignment.CENTER:
                    y_offset = (self._max_height - element._height) / 2
                case VerticalAlignment.BOTTOM:
                    y_offset = (self._max_height - element._height)

            element_position = (self._position[0] + x_offset, self._position[1] + y_offset)
            element.set_position(element_position)
            x_offset += element._width + self._padding
