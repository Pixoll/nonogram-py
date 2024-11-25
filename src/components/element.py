from abc import ABC, abstractmethod
from typing import Self

from pygame import Surface

from events import Event


class Element(ABC):
    _width: int
    _height: int
    _position: tuple[int, int]

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._position = (0, 0)

    @property
    def size(self) -> tuple[int, int]:
        return self._width, self._height

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    def set_size(self, width: int, height: int):
        self._width = width
        self._height = height

    def contains(self, position: tuple[int, int]) -> bool:
        mx, my = position
        x, y = self._position
        w, d = self.size
        return x <= mx <= x + w and y <= my <= y + d

    @abstractmethod
    def set_position(self, position: tuple[int, int]) -> Self:
        pass

    @abstractmethod
    def on_any_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def render(self, window: Surface) -> None:
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__} {self._width}x{self._height} {self._position}"
