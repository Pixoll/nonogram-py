from typing import Self

import pygame

from components.element import Element
from events import Event


class ColorBlock(Element):
    _color: tuple[int, int, int]
    _position: tuple[int, int]
    _surface: pygame.Surface

    def __init__(self, size: int, color: tuple[int, int, int]) -> None:
        super().__init__(size, size)
        self._color = color
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill(self._color)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def set_color(self, color: tuple[int, int, int]) -> Self:
        self._color = color
        self._surface.fill(color)
        return self

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    def on_all_events(self, event: Event) -> None:
        return

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._surface, self._position)
