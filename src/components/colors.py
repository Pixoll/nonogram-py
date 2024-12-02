from typing import Self

import pygame

from components import Column
from components.colored_block import ColoredBlock
from components.element import Element
from events import Event, EventType, MouseButton


class Colors(Element):
    def __init__(self, block_size: int, padding: int) -> None:
        colors = Colors._generate_colors()

        super().__init__(block_size * 5, len(colors) * (block_size + padding) - padding)

        self._block_size = block_size
        self._selected_color = (255, 0, 0)
        self._column: Column[ColoredBlock] = Column().set_padding(padding)

        for color in colors:
            self._column.add_element(ColoredBlock(block_size * 5, block_size, color))

        self._selected_block = self._column[-1]
        self._selected_block.toggle_selected()

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill((255, 255, 255, 128))

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._column.set_position(position)
        return self

    def set_active(self, active: bool) -> None:
        self._selected_block.set_active(active)

    @staticmethod
    def _generate_colors() -> list[tuple[int, int, int]]:
        colors: list[tuple[int, int, int]] = [(255, 0, 0)]

        steps = 8
        shift = 255 // steps
        step_range = range(0, steps)

        for (rm, gm, bm) in ((0, 0, 1), (-1, 0, 0), (0, 1, 0), (0, 0, -1), (1, 0, 0), (0, -1, 0)):
            for _ in step_range:
                r, g, b = colors[-1]
                color = (r + (rm * shift), g + (gm * shift), b + (bm * shift))
                colors.append(color)

        return colors

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for block in self._column:
            if block.contains(pygame.mouse.get_pos()):
                self._selected_block.toggle_selected()
                self._selected_block = block
                self._selected_color = block.color
                block.toggle_selected()
                break

    def get_selected_color(self) -> tuple[int, int, int]:
        return self._selected_color

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._column.render(screen)
