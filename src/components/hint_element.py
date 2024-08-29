import pygame
from components.board import Board
from components.element import Element

class HintElement(Element):
    def __init__(self, dimension:int, size:int):
        super().__init__(dimension,dimension)
        self.size = size

    def draw_hints(self, board:Board):
        size_board = board.size

