from typing import Self

import pygame

from components import Column
from components.colored_block import ColoredBlock
from components.element import Element
from events import Event, EventType, MouseButton


class RecentColors(Element):
    def __init__(self, block_size: int, padding: int) -> None:
        super().__init__(block_size, block_size * 6 + padding * 5)
        self._block_size = block_size
        self._padding = padding
        self._current_color = (255, 255, 255)
        self._recent_colors = [(255, 255, 255) for _ in range(6)]

        self._column = Column()
        for color in self._recent_colors:
            self._column.add_element(ColoredBlock(block_size, color))
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._column.set_position(position)
        return self

    def add_color(self, color: tuple[int, int, int]) -> None:
        if color not in self._recent_colors:
            self._recent_colors.insert(0, color)
            self._recent_colors.pop()

            for i in range(len(self._column)):
                self._column[i].set_color(self._recent_colors[i])

    def get_current_color(self) -> tuple[int, int, int]:
        return self._current_color

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for block in self._column:
            if block.contains(pygame.mouse.get_pos()):
                self._current_color = block.color
                break

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._column.render(screen)
