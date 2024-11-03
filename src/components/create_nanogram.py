from typing import Self, TypeAlias

import pygame
from PIL import Image
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.row import Row
from core.nonogram import Nonogram
from events import Event, EventType, MouseButton

rgb_t: TypeAlias = tuple[int, int, int]


class CreateNanogram(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _grid: Row[Column[Block]]
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

        self._background_color = (192, 192, 192)
        self._padding = padding
        self._grid = Row()
        self._grid_position = (0, 0)
        self._block_size = block_size
        self._selected_color = (0, 0, 0)
        self._cwidth = width
        self._cheight = height
        self._name = ""

        for i in range(width):
            column: Column[Block] = Column()
            for j in range(height):
                column.add_element(Block(block_size, block_size, (255, 255, 255)))
            self._grid.add_element(column)
            column.set_padding(padding)

        self._grid.set_padding(padding)

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

    def set_selected_color(self, color: tuple[int, int, int]) -> Self:
        self._selected_color = color
        return self

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

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        mouse_pos = pygame.mouse.get_pos()

        for column in self._grid:
            for block in column:
                if not block.contains(mouse_pos):
                    continue

                block.set_state(Block.State(int(event.button == MouseButton.LEFT)), self._selected_color)

    def set_name(self, name: str) -> None:
        self._name = name

    def randomizer(self) -> None:
        unique_colors = set(
            block.color for column in self._grid for block in column
            if block.color != (255, 255, 255)
        )

        colors = list(unique_colors)
        if not colors:
            print("No available colors to generate randomized nonogram.")
            return None

        random_nonogram = Nonogram.generate((self._cwidth, self._cheight), colors)

        for y in range(self._cheight):
            for x in range(self._cwidth):
                color = random_nonogram[x, y]
                if color is not None:
                    self._grid[x][y].set_background_color(color)
                else:
                    self._grid[x][y].set_background_color((255, 255, 255))

        print("Generated randomized nonogram")

    def is_valid_nonogram(self) -> bool:
        unique_colors = set()

        for column in self._grid:
            row_has_color = False
            for block in column:
                if block.color != (255, 255, 255):
                    row_has_color = True
                    unique_colors.add(block.color)
            if not row_has_color:
                return False

        num_rows = len(self._grid[0])
        for row_idx in range(num_rows):
            col_has_color = False
            for column in self._grid:
                if column[row_idx].color != (255, 255, 255):
                    col_has_color = True
                    unique_colors.add(column[row_idx].color)
            if not col_has_color:
                return False

        if len(unique_colors) > 256:
            return False

        return True

    def generate_from_image(self, image_path: str, colors: int = 256) -> None:
        with Image.open(image_path) as img:
            resized_img = img.resize((self._cwidth, self._cheight), Image.NEAREST).convert("RGB")

        image_matrix = []
        pixels = resized_img.load()
        for y in range(self._cheight):
            row = []
            for x in range(self._cwidth):
                row.append(pixels[x, y])
            image_matrix.append(row)

        for y in range(self._cheight):
            for x in range(self._cwidth):
                color = image_matrix[y][x]
                if color != (255, 255, 255):
                    self._grid[x][y].set_background_color(color)
                else:
                    self._grid[x][y].set_background_color((255, 255, 255))

        print("Generated nonogram from image")

    def save(self) -> None:
        if not self.is_valid_nonogram():
            print("Invalid nonogram")
            return

        print("Valid nonogram")

        matrix: list[list[rgb_t | None]] = []
        for column in self._grid:
            matrix.append([
                block.color if block.color != (255, 255, 255) else None
                for block in column
            ])

        nonogram = Nonogram.from_matrix(matrix, self._name)
        nonogram.save(self._name)
