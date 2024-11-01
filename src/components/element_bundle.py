from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pygame import Surface

from components.element import Element

T = TypeVar("T", bound=Element)
S = TypeVar("S", bound="ElementBundle")


class ElementBundle(Element, ABC, Generic[T]):
    _elements: list[T]
    _padding: int

    def __init__(self):
        super().__init__(0, 0)

        self._elements = []
        self._padding = 0

    def add_element(self: S, element: T) -> S:
        self._elements.append(element)
        self._update_size()
        self._update_positions()
        return self

    def set_position(self: S, position: tuple[int, int]) -> S:
        self._position = position
        self._update_positions()
        return self

    def set_padding(self: S, padding: int) -> S:
        self._padding = padding
        self._update_positions()
        self._update_size()
        return self

    def __iter__(self):
        for element in self._elements:
            yield element

    def render(self, window: Surface) -> None:
        for element in self._elements:
            element.render(window)

    @abstractmethod
    def _update_size(self) -> None:
        pass

    @abstractmethod
    def _update_positions(self) -> None:
        pass
