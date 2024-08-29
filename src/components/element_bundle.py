from abc import ABC, abstractmethod
from typing import Self

from pygame import Surface

from components.element import Element


class ElementBundle(Element, ABC):
    _elements: list[Element | Self]
    _padding: int

    def __init__(self):
        super().__init__(0, 0)

        self._elements = []
        self._padding = 0

    def add_element(self, element: Element | Self) -> Self:
        self._elements.append(element)
        self._update_size()
        self._update_positions()
        return self

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._update_positions()
        return self

    def set_padding(self, padding: int) -> Self:
        self._padding = padding
        self._update_positions()
        self._update_size()
        return self

    @property
    def elements(self) -> tuple[Element | Self, ...]:
        return tuple(self._elements)

    def render(self, window: Surface) -> None:
        for element in self._elements:
            element.render(window)

    @abstractmethod
    def _update_size(self) -> None:
        pass

    @abstractmethod
    def _update_positions(self) -> None:
        pass
