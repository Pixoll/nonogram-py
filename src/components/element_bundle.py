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
        self.update_positions()
        return self

    def set_position(self: S, position: tuple[int, int]) -> S:
        self._position = position
        self.update_positions()
        return self

    def set_padding(self: S, padding: int) -> S:
        self._padding = padding
        self.update_positions()
        self._update_size()
        return self

    def set_hidden(self: S, hidden: bool) -> S:
        self._hidden = hidden
        for element in self._elements:
            element.set_hidden(hidden)
        return self

    def __iter__(self):
        for element in self._elements:
            yield element

    def __getitem__(self, index: int) -> T:
        return self._elements[index]

    def __setitem__(self, index: int, value: T) -> None:
        self._elements[index] = value

    def __len__(self) -> int:
        return len(self._elements)

    def render(self, window: Surface) -> None:
        if self.hidden:
            return

        for element in self._elements:
            element.render(window)

    @abstractmethod
    def _update_size(self) -> None:
        pass

    @abstractmethod
    def update_positions(self) -> None:
        pass
