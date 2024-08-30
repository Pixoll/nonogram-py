from components import Element
from components.board import Board
from core.nonogram import Nonogram
from events import Event


class NonogramElement(Element):
    _nonogram: Nonogram
    _cell_size: int
    _margin: int
    _colors: tuple[tuple[int, int, int], ...]
    _board: Board

    def __init__(self, nonogram: Nonogram):
        super().__init__(*nonogram.size)
        self._nonogram = nonogram
        self._cell_size = 10
        self._margin = 10
        self._colors = nonogram.used_colors
        self._board = Board(nonogram, 25, 0)

    @property
    def board(self) -> Board:
        return self._board

    def set_position(self, position: tuple[int, int]):
        return

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window):
        self._board.render(window)
        return
