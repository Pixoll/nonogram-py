from abc import ABC
from enum import auto, Enum
from typing import Self

from components.element import Element


class ChildAlignment(Enum):
    TOP_LEFT = auto()
    TOP_CENTER = auto()
    TOP_RIGHT = auto()
    CENTER_LEFT = auto()
    CENTER = auto()
    CENTER_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_CENTER = auto()
    BOTTOM_RIGHT = auto()


class ElementWithChild(Element, ABC):
    _child: Element | None
    _child_alignment: ChildAlignment

    def __init__(self, width: int, height: int, alignment: ChildAlignment = ChildAlignment.CENTER):
        super().__init__(width, height)

        self._child = None
        self._child_alignment = alignment

    def set_child(self, child: Element) -> Self:
        self._child = child
        self._update_child_position()
        return self

    def set_child_alignment(self, alignment: ChildAlignment) -> Self:
        self._child_alignment = alignment
        self._update_child_position()
        return self

    def _update_child_position(self) -> None:
        if self._child is None:
            return

        width, height = self._child.size
        position: tuple[int, int] = (0, 0)

        match self._child_alignment:
            case ChildAlignment.TOP_LEFT:
                position = (0, 0)
            case ChildAlignment.TOP_CENTER:
                position = ((self._width - width) // 2, 0)
            case ChildAlignment.TOP_RIGHT:
                position = (self._width - width, 0)
            case ChildAlignment.CENTER_LEFT:
                position = (0, (self._height - height) // 2)
            case ChildAlignment.CENTER:
                position = ((self._width - width) // 2, (self._height - height) // 2)
            case ChildAlignment.CENTER_RIGHT:
                position = (self._width - width, (self._height - height) // 2)
            case ChildAlignment.BOTTOM_LEFT:
                position = (0, self._height - height)
            case ChildAlignment.BOTTOM_CENTER:
                position = ((self._width - width) // 2, self._height - height)
            case ChildAlignment.BOTTOM_RIGHT:
                position = (self._width - width, self._height - height)

        child_position = (position[0] + self._position[0], position[1] + self._position[1])
        self._child.set_position(child_position)