import pygame
from components.element import Element
from components.color_block import ColorBlock
from events import Event

class ColorPicker(Element):
    _surface: pygame.Surface
    _colors: tuple[tuple[int, int, int], ...]
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _size_block: int

    def __init__(self, colors: tuple[tuple[int, int, int], ...], padding: int) -> None:
        cols = 4
        rows = len(colors) // cols + (1 if len(colors) % cols > 0 else 0)
        super().__init__(cols * 25, rows * 25)

        self._colors = colors
        self._size_block = 55
        self._padding = padding
        self._position = (1000, 300)
        self._background_color = (229, 229, 229)

        width = cols * (self._size_block + padding)
        height = rows * (self._size_block + padding)
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

        for row_index in range(rows):
            for col_index in range(cols):
                color_index = row_index * cols + col_index
                if color_index < len(colors):
                    color_block = ColorBlock(self._size_block, self._size_block, self._colors[color_index])
                    block_x = col_index * (self._size_block + padding)
                    block_y = row_index * (self._size_block + padding)
                    color_block.set_position((block_x, block_y))
                    color_block.render(self._surface)

    def set_position(self, position: tuple[int, int]):
        self._position = position

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
