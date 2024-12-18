from typing import Self, TypeAlias

import pygame
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.row import Row
from core import Nonogram, NonogramLoader
from events import Event, EventType, MouseButton

rgb_t: TypeAlias = tuple[int, int, int]


class CreateNanogram(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _grid: Column[Row[Block]]
    _grid_position: tuple[int, int]
    _block_size: int
    _selected_color: tuple[int, int, int]
    _width: int
    _height: int
    _name: str

    def __init__(self, width: int, height: int, padding: int, size: int):
        max_dimension = max(width, height)
        block_size = (size // max_dimension) - 1

        super().__init__(
            width * (block_size + padding) + padding,
            height * (block_size + padding) + padding
        )

        self._background_color = (255, 255, 255, 128)
        self._padding = padding
        self._grid = Column().set_padding(padding)
        self._grid_position = (0, 0)
        self._block_size = block_size
        self._selected_color = (0, 0, 0)
        self._cwidth = width
        self._cheight = height
        self._name = ""

        for i in range(width):
            row: Row[Block] = Row().set_padding(padding)
            for j in range(height):
                row.add_element(Block(block_size, block_size, (255, 255, 255)))
            self._grid.add_element(row)

        self._width = self._grid.size[0]
        self._height = self._grid.size[1]

        self._surface = Surface((self.size[0] + padding * 2, self.size[1] + padding * 2), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._grid_position = self._position
        self._grid.set_position(self._grid_position)
        return self

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        return self

    @property
    def selected_color(self) -> tuple[int, int, int]:
        return self._selected_color

    def set_selected_color(self, color: tuple[int, int, int]) -> Self:
        self._selected_color = color
        return self

    @property
    def grid_size(self) -> tuple[int, int]:
        return self._cwidth, self._cheight

    def get_block(self, mouse_position: tuple[int, int]) -> Block:
        x, y = self._get_grid_position(mouse_position)
        return self._grid[x][y]

    def render(self, window: Surface):
        window.blit(self._surface, (self.position[0] - self._padding, self._position[1] - self._padding))
        self._grid.render(window)

    def clear(self) -> None:
        for column in self._grid:
            for block in column:
                block.set_background_color((255, 255, 255))

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        is_left_click = event.button == MouseButton.LEFT
        is_right_click = event.button == MouseButton.RIGHT

        if not is_left_click and not is_right_click:
            return

        mouse_pos = pygame.mouse.get_pos()

        if not self._grid.contains(mouse_pos):
            return

        x, y = self._get_grid_position(mouse_pos)
        block = self._grid[x][y]

        new_state = (Block.State.EMPTY if is_right_click or (is_left_click and block.state == Block.State.COLORED)
                     else Block.State.COLORED)
        block.set_state(new_state, self._selected_color)

    def set_name(self, name: str) -> None:
        self._name = name

    def randomizer(self) -> None:
        unique_colors = set(
            block.color for column in self._grid for block in column
            if block.color != (255, 255, 255)
        )

        colors = list(unique_colors)
        if not colors:
            raise ValueError("No available colors to generate randomized nonogram.")

        random_nonogram = Nonogram.matrix_randomized((self._cwidth, self._cheight), colors)

        for y in range(self._cheight):
            for x in range(self._cwidth):
                color = random_nonogram[y][x]
                if color is not None:
                    self._grid[y][x].set_background_color(color)
                else:
                    self._grid[y][x].set_background_color((255, 255, 255))

    def has_more_than_128_colors(self) -> bool:
        unique_colors = set()

        for column in self._grid:
            for block in column:
                if block.color != (255, 255, 255):
                    unique_colors.add(block.color)

        return len(unique_colors) > 128

    def has_empty_row_or_column_in_between(self) -> bool:
        matrix = self._get_trimmed_matrix()

        for row in matrix:
            if all(cell is None for cell in row):
                return True

        for col in zip(*matrix):
            if all(cell is None for cell in col):
                return True

        return False

    def generate_from_image(self, image_path: str, colors: int = 128) -> None:
        image_matrix = Nonogram.matrix_from_image(image_path, colors, (self._cwidth, self._cheight))

        for y in range(self._cheight):
            for x in range(self._cwidth):
                color = image_matrix[y][x]
                if color is not None and color != (255, 255, 255):
                    self._grid[y][x].set_background_color(color)
                else:
                    self._grid[y][x].set_background_color((255, 255, 255))

    def is_empty(self) -> bool:
        for column in self._grid:
            for block in column:
                if block.color != (255, 255, 255):
                    return False
        return True

    def is_nameless(self) -> bool:
        return self._name == ""

    def save(self) -> None:
        matrix = self._get_trimmed_matrix()
        nonogram = Nonogram(matrix, "user_made", nonogram_name=self._name)
        NonogramLoader.store_and_save(nonogram)

    def _get_trimmed_matrix(self) -> list[list[rgb_t | None]]:
        matrix: list[list[rgb_t | None]] = []
        for row in self._grid:
            matrix.append([
                block.color if block.color != (255, 255, 255) else None
                for block in row
            ])

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        top, bottom, left, right = rows, 0, cols, 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] is not None:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        return [row[left:right + 1] for row in matrix[top:bottom + 1]]

    def _get_grid_position(self, mouse_pos: tuple[int, int]) -> tuple[int, int]:
        return (
            min((mouse_pos[1] - self._grid.position[1]) // (self._block_size + self._padding), self._cwidth - 1),
            min((mouse_pos[0] - self._grid.position[0]) // (self._block_size + self._padding), self._cheight - 1)
        )
