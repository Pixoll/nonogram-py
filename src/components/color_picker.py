import pygame
from components.column import Column
from components.element import Element
from components.row import Row
from components.color_block import ColorBlock
from events import Event

class ColorPicker(Element):
    _surface: pygame.Surface
    _colors: tuple[tuple[int, int, int], ...]
    _size: int
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _row: Row

    def __init__(self, colors: tuple[tuple[int, int, int], ...], padding: int) -> None:
        cols = 4
        rows = len(colors) // cols + (1 if len(colors) % cols > 0 else 0)
        super().__init__(cols * 25, rows * 25)

        self._colors = colors
        self._size = 25
        self._padding = padding
        self._position = (700, 300)
        self._background_color = (229, 229, 229)
        self._row = Row()

        for row_index in range(rows):
            column = Column()
            for col_index in range(cols):
                color_index = row_index * cols + col_index
                if color_index < len(colors):
                    color_block = ColorBlock(self._size, self._size, self._colors[color_index])
                    column.add_element(color_block)
            column.set_padding(padding)
            self._row.add_element(column)

        self._row.set_padding(padding)

        width = cols * (self._size + padding)
        height = rows * (self._size + padding)
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]):
        self._position = position

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._row.render(screen)

