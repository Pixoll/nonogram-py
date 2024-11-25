from enum import auto, Enum
from typing import Self, TypeVar

from components.element import Element
from components.element_bundle import ElementBundle
from events import Event


class HorizontalAlignment(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


T = TypeVar("T", bound=Element)


class Column(ElementBundle[T]):
    _alignment: HorizontalAlignment
    _max_width: int

    def __init__(self):
        super().__init__()
        self._alignment = HorizontalAlignment.CENTER
        self._max_width = 0

    def set_alignment(self, alignment: HorizontalAlignment) -> Self:
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

        self._height = sum(element._height for element in self._elements) + self._padding * (len(self._elements) - 1)
        self._width = max(element._width for element in self._elements)
        self._max_width = self._width

    def _update_positions(self) -> None:
        y_offset = 0

        for element in self._elements:
            x_offset = 0

            match self._alignment:
                case HorizontalAlignment.LEFT:
                    x_offset = 0
                case HorizontalAlignment.CENTER:
                    x_offset = (self._max_width - element._width) // 2
                case HorizontalAlignment.RIGHT:
                    x_offset = (self._max_width - element._width)

            element_position = (self._position[0] + x_offset, self._position[1] + y_offset)
            element.set_position(element_position)
            y_offset += element._height + self._padding
