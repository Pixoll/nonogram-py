from typing import Self
import pygame
from components.element import Element
from events import Event

class BlockWithImage(Element):
    _position: tuple[int, int]
    _surface: pygame.Surface
    _image: pygame.Surface

    def __init__(self, width: int, height: int, image: str = None) -> None:
        super().__init__(width, height)
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._image = pygame.transform.scale(pygame.image.load(f'assets/textures/{image}'), self.size)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def on_all_events(self, event: Event) -> None:
        return

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self._position)


