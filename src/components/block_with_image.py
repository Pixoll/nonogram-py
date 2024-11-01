from typing import Self

import pygame

from assets import TextureManager
from components.element import Element
from events import Event


class BlockWithImage(Element):
    _position: tuple[int, int]
    _surface: pygame.Surface
    _image: pygame.Surface

    def __init__(self, width: int, height: int, texture_name: str = None) -> None:
        super().__init__(width, height)
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._image = self._image = TextureManager.get(texture_name, self.size)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def on_any_event(self, event: Event) -> None:
        return

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self._position)
