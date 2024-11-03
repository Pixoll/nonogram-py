from typing import Self

import pygame

from components import Column, HorizontalAlignment, Row, VerticalAlignment
from components.colored_block import ColoredBlock
from components.element import Element
from events import Event, EventType, MouseButton


class Colors(Element):
    def __init__(self, block_size: int, padding: int) -> None:
        cant_columns = 3
        cant_colors = 85

        super().__init__(cant_columns * (block_size + padding) - padding,
                         cant_colors * (block_size + padding) - padding)
        self._block_size = block_size
        self._selected_color = None  # Almacena el color seleccionado
        self._column1: Column[ColoredBlock] = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column2: Column[ColoredBlock] = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column3: Column[ColoredBlock] = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column4: Column[ColoredBlock] = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column5: Column[ColoredBlock] = Column().set_alignment(HorizontalAlignment.CENTER)

        colors = Colors._generate_colors()

        for color in colors:
            self._column1.add_element(ColoredBlock(block_size, color))
            self._column2.add_element(ColoredBlock(block_size, color))
            self._column3.add_element(ColoredBlock(block_size, color))
            self._column4.add_element(ColoredBlock(block_size, color))
            self._column5.add_element(ColoredBlock(block_size, color))
        self._row: Row[Column[ColoredBlock]] = (Row()
                                                .set_alignment(VerticalAlignment.CENTER)
                                                .add_element(self._column1)
                                                .add_element(self._column2)
                                                .add_element(self._column3)
                                                .add_element(self._column4)
                                                .add_element(self._column5))

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    @staticmethod
    def _generate_colors() -> list[tuple[int, int, int]]:
        colors: list[tuple[int, int, int]] = [(255, 0, 0)]

        steps = 15
        shift = 255 // 15
        step_range = range(0, steps)

        for (rm, gm, bm) in ((0, 0, 1), (-1, 0, 0), (0, 1, 0), (0, 0, -1), (1, 0, 0), (0, -1, 0)):
            for _ in step_range:
                r, g, b = colors[-1]
                color = (r + (rm * shift), g + (gm * shift), b + (bm * shift))
                colors.append(color)

        colors.append((255, 0, 0))

        return colors

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row:
            for block in column:
                if block.contains(pygame.mouse.get_pos()):
                    self._selected_color = block.color
                    break

    def get_selected_color(self) -> tuple[int, int, int] | None:
        return self._selected_color

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._row.render(screen)
