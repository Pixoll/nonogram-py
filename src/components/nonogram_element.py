import pygame
from components.board import Board
from core.nonogram import Nonogram
from components import Element


class NonogramElement(Element):
    def __init__(self, nonogram: Nonogram):
        super().__init__(*nonogram.size)
        self.nonogram = nonogram
        self.cell_size = 10
        self.margin = 10
        self.grid_width = nonogram.size[0]
        self.grid_height = nonogram.size[1]
        self.colors = nonogram.used_colors
        self.board = Board(self.grid_width, self.grid_height,50,5)

    def render(self, window):
        self.board.render(window)
        return

    def get_size(self) -> tuple[int, int]:
        return self.grid_width, self.grid_height

    def set_position(self, position: tuple[int, int]):
        return





