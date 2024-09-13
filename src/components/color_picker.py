import pygame

from components.color_block import ColorBlock
from components.column import Column
from components.element import Element
from components.nonogram_element import NonogramElement
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton


class ColorPicker(Element):
    _surface: pygame.Surface
    _row: Row
    _padding: int
    _position: tuple[int, int]
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _size_block: int
    _selected_block: ColorBlock
    _nonogram_element: NonogramElement

    def __init__(
            self,
            nonogram_element: NonogramElement,
            colors: tuple[tuple[int, int, int], ...],
            block_size: int,
            padding: int
    ) -> None:
        cols = 4
        rows = len(colors) // cols
        if len(colors) % cols > 0:
            rows += 1
        super().__init__(cols * 25, rows * 25)

        self._colors = colors
        self._size_block = 50
        self._padding = padding
        self._background_color = (229, 229, 229)
        self._row = Row().set_alignment(VerticalAlignment.TOP)
        self._nonogram_element = nonogram_element
        width = cols * (self._size_block + padding)
        height = rows * (self._size_block + padding)

        for i in range(cols):
            column = Column()
            for j in range(rows):
                index = i + j * cols
                if index < len(colors):
                    column.add_element(ColorBlock(self._size_block, colors[index]))
            self._row.add_element(column)
            column.set_padding(padding)

        self._row.set_padding(padding)
        self.set_position((1500, 400))

        self._selected_block = ColorBlock(self._size_block, colors[0])
        self._selected_block.set_position((self._position[0] + 25, self._position[1] + 200))

        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(self._background_color)

    def set_position(self, position: tuple[int, int]):
        self._position = position
        self._row.set_position(position)

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row.elements:
            for block in column.elements:
                if block.contains(pygame.mouse.get_pos()):
                    # noinspection PyTypeChecker
                    b: ColorBlock = block
                    color = b.color
                    self._selected_block.set_color(color)
                    self._nonogram_element.set_selected_color(color)

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._selected_block.render(screen)
        self._row.render(screen)
