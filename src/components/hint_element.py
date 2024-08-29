from typing import Self

from pygame import Surface

from components.board import Board
from components.element import Element
from events import Event


class HintElement(Element):

    def __init__(self, size: int):
        super().__init__(size, size)

    def render_hints(self, board: Board):
        size_board = board.size

    def set_position(self, position: tuple[int, int]) -> Self:
        pass

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        pass
