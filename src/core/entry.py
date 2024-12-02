from enum import auto, IntEnum

from core.nonogram import Nonogram


class NonogramSize(IntEnum):
    SMALL = 0
    MEDIUM = auto()
    BIG = auto()
    HUGE = auto()


class Entry:
    _width: int
    _height: int
    _colors: int
    _size: NonogramSize
    _nonogram: Nonogram | None

    def __init__(self, width: int, height: int, colors: int):
        self._width = width
        self._height = height
        self._colors = colors
        self._size = NonogramSize(min(width * height, 2000) // 501)
        self._nonogram = None

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def colors(self) -> int:
        return self._colors

    @property
    def size(self) -> NonogramSize:
        return self._size

    @property
    def nonogram(self) -> Nonogram | None:
        return self._nonogram

    def __repr__(self) -> str:
        return f"{self._size.name} ({self._width}x{self._height}) {self._colors}"
