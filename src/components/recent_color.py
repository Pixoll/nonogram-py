from typing import Self

import pygame

from components.colored_block import ColoredBlock
from components.column import Column
from components.element import Element
from components.row import Row, VerticalAlignment
from events import Event, EventType, MouseButton


class RecentColors(Element):
    def __init__(self, block_size: int, padding: int, default_color: tuple[int, int, int]) -> None:
        super().__init__(block_size, 10 * (block_size + padding) - padding)
        self._block_size = block_size
        self._current_color = (255, 255, 255)
        self._recent_colors = [(255, 255, 255) for _ in range(10)]
        self._number_of_colors = 0

        self._column: Column[ColoredBlock] = Column().set_padding(padding)
        for color in self._recent_colors:
            self._column.add_element(ColoredBlock(block_size, block_size, color))

        self._selected_block = self._column[0]
        self._selected_block.toggle_selected()

        self._row: Row[Column] = Row().set_alignment(VerticalAlignment.TOP).add_element(self._column)

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill((255, 255, 255, 128))

        self.add_color(default_color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    @property
    def is_active(self) -> bool:
        return self._selected_block.is_active

    def set_active(self, active: bool) -> None:
        self._selected_block.set_active(active)

    def add_color(self, color: tuple[int, int, int]) -> None:
        if color not in self._recent_colors:
            self._recent_colors.insert(0, color)
            self._recent_colors.pop()
            self._number_of_colors = min(self._number_of_colors + 1, 10)

            for i in range(len(self._column)):
                self._column[i].set_color(self._recent_colors[i])

    def select_color(self, color: tuple[int, int, int] | None = None) -> None:
        self._selected_block.toggle_selected()

        index: int
        try:
            index = self._recent_colors.index(color)
        except ValueError:
            index = 0

        self._selected_block = self._column[index]
        self._current_color = self._selected_block
        self._selected_block.toggle_selected()

    def get_current_color(self) -> tuple[int, int, int]:
        return self._current_color

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for i in range(0, self._number_of_colors):
            block = self._column[i]
            if block.contains(pygame.mouse.get_pos()):
                self._selected_block.toggle_selected()
                self._selected_block = block
                self._current_color = block.color
                block.toggle_selected()
                break

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)

        for i in range(0, self._number_of_colors):
            self._column[i].render(screen)
