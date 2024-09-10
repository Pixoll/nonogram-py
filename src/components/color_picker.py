import pygame
from components.element import Element
from components.color_block import ColorBlock
from components.row import Row, VerticalAlignment
from components.column import Column
from events import Event

class ColorPicker(Element):
    _surface: pygame.Surface
    _row: Row
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _size_block: int
    _color_selected: ColorBlock

    def __init__(self, colors: tuple[tuple[int, int, int], ...], padding: int) -> None:
        cols = 4
        rows = len(colors)//cols
        if len(colors) % cols > 0:
            rows += 1
        super().__init__(cols * 25, rows * 25)

        self._colors = colors
        self._size_block = 50
        self._padding = padding
        self._background_color = (229, 229, 229)
        self._row = Row().set_alignment(VerticalAlignment.TOP)
        self._color_selected = ColorBlock(self._size_block,self._size_block,(1,1,1))
        width = cols * (self._size_block + padding)
        height = rows * (self._size_block + padding)

        for i in range(cols):
            column = Column()
            for j in range(rows):
                if i * rows + j < len(colors):
                    print(i * rows + j)
                    column.add_element(ColorBlock(self._size_block, self._size_block, colors[i * rows + j]))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)
        self.set_position((1000,300))
        self._color_selected.set_position((self._position[0] + 25, self._position[1]+200))
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)

        self._surface.fill(self._background_color)


    def set_position(self, position: tuple[int, int]):
        self._position = position
        self._row.set_position(position)

    def on_all_events(self, event: Event) -> tuple[int, int, int] | tuple[int, int, int, int]:
        for column_or_block in self._row.elements:
            if isinstance(column_or_block, ColorBlock):
                color = column_or_block.on_all_events(event)
                if color:
                    self._color_selected.set_color(color)
                    self._color_selected._surface.fill(color)
                    return color
            else:
                for block in column_or_block.elements:
                    color = block.on_all_events(event)
                    if color:
                        self._color_selected.set_color(color)
                        self._color_selected._surface.fill(color)
                        return color

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._color_selected.render(screen)
        self._row.render(screen)
