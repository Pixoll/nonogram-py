from enum import auto, IntEnum

from core.nonogram import Nonogram
from core.types import nonogram_type_t


class NonogramSize(IntEnum):
    SMALL = 0
    MEDIUM = auto()
    BIG = auto()
    HUGE = auto()


class Entry:
    _nonogram_type: nonogram_type_t
    _nonogram_id: int
    _width: int
    _height: int
    _colors: int
    _size: NonogramSize
    _nonogram: Nonogram | None
    _in_progress: bool

    def __init__(
            self,
            nonogram_type: nonogram_type_t,
            nonogram_id: int,
            width: int,
            height: int,
            colors: int,
            in_progress: bool
    ):
        self._nonogram_type = nonogram_type
        self._nonogram_id = nonogram_id
        self._width = width
        self._height = height
        self._colors = colors
        self._size = NonogramSize(min(width * height, 2000) // 501)
        self._nonogram = None
        self._in_progress = in_progress

    @property
    def nonogram_type(self) -> nonogram_type_t:
        return self._nonogram_type

    @property
    def nonogram_id(self) -> int:
        return self._nonogram_id

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

    @property
    def in_progress(self) -> bool:
        return self._in_progress

    def __repr__(self) -> str:
        return f"{self._size.name} ({self._width}x{self._height}) {self._colors}"
