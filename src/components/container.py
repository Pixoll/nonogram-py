from typing import Self

import pygame

from components.element_with_child import ElementWithChild
from events import Event


class Container(ElementWithChild):
    _surface: pygame.Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_width: int
    _image: pygame.Surface | None

    def __init__(self, width: int, height: int):
        super().__init__(width, height)

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._background_color = (0, 0, 0, 0)
        self._border_color = (255, 255, 255)
        self._border_width = 1

        self._surface.fill(self._background_color)
        self._draw_border()

        self._image = None

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        self._draw_border()
        return self

    def set_border(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._border_color = color
        self._draw_border()
        return self

    def set_border_width(self, border_width: int) -> Self:
        self._border_width = border_width
        self._draw_border()
        return self

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._update_child_position()
        return self

    def set_image(self, image_path: str) -> Self:
        self._image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(self._image, self.size)
        self._surface.blit(self._image, (0, 0))
        return self

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window: pygame.Surface) -> None:
        if self._image:
            self._surface.blit(self._image, (0, 0))

        window.blit(self._surface, self._position)

        if self._child:
            self._child.render(window)

    def _draw_border(self) -> None:
        pygame.draw.rect(self._surface, self._border_color, self._surface.get_rect(), self._border_width)
