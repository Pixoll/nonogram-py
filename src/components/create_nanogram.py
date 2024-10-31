import json
from typing import Self, TypeAlias

import pygame
from pygame import Surface

from components.block import Block
from components.column import Column
from components.element import Element
from components.row import Row
from events import Event, EventType, MouseButton

rgb_t: TypeAlias = tuple[int, int, int]


class CreateNanogram(Element):
    _surface: Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _padding: int
    _grid: Row
    _grid_position: tuple[int, int]
    _block_size: int
    _selected_color: tuple[int, int, int]
    _width: int
    _height: int
    _colors: list[str]
    _name: str

    def __init__(self, width: int, height: int, padding: int):
        max_dimension = max(width, height)
        block_size = (519 - padding * (max_dimension + 1)) // max_dimension

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
        self._colors = []
        self._cwidth = int
        self._cheight = int
        self._name = ''

        for i in range(width):
            column = Column()
            for j in range(height):
                column.add_element(Block(block_size, block_size, (255, 255, 255)))
            self._grid.add_element(column)
            column.set_padding(padding)

        self._grid.set_padding(padding)

        self._width = self._grid.size[0]
        self._height = self._grid.size[1]
        self._cheight = height
        self._cwidth = width

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
        for column in self._grid.elements:
            for block in column.elements:
                # noinspection PyTypeChecker
                b: Block = block
                b.set_background_color((255, 255, 255))

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        mouse_pos = pygame.mouse.get_pos()

        for column in self._grid.elements:
            for block in column.elements:
                # noinspection PyTypeChecker
                b: Block = block
                if not b.contains(mouse_pos):
                    continue

                b.set_state(Block.State(int(event.button == MouseButton.LEFT)), self._selected_color)

    def set_name(self, name: str) -> None:
        self._name = name

    # TODO implement into Nonogram class, this shouldn't be here
    def save(self, nonogram_id: int = 1) -> None:
        self._colors = []
        mask = ''

        for column in self._grid.elements:
            for block in column.elements:
                # noinspection PyTypeChecker
                b: Block = block
                hex_color = "%02x%02x%02x" % b.color

                if hex_color != '#ffffff':
                    if hex_color not in self._colors:
                        self._colors.append(hex_color)
                    color_index = self._colors.index(hex_color) + 1
                    mask += str(color_index)
                else:
                    mask += ' '

        palette = {str(i + 1): color[1:] for i, color in enumerate(self._colors)}

        nonogram_data = {
            "id": nonogram_id,
            "mask": mask,
            "width": self._cheight,
            "height": self._cwidth,
            "palette": palette,
            "player_mask": None,
            "completed": False
        }

        with open(f"nonograms/pre_made/0.json", 'w') as json_file:
            json.dump(nonogram_data, json_file, indent=4)
