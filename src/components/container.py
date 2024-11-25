from typing import Generic, Self, TypeVar

import pygame

from assets import TextureManager
from components.element import Element
from components.element_with_child import ElementWithChild
from events import Event

T = TypeVar("T", bound=Element)


class Container(ElementWithChild[T], Generic[T]):
    _surface: pygame.Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_width: int
    _corner_radius: int
    _image: pygame.Surface | None

    def __init__(self, width: int, height: int, corner_radius: int = -1):
        super().__init__(width, height)

        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._background_color = (0, 0, 0, 0)
        self._border_color = (0, 0, 0, 0)
        self._border_width = 1
        self._corner_radius = corner_radius

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
        self.update_child_position()
        return self

    def set_image(self, image_path: str, stretch: bool = True) -> Self:
        if stretch:
            self._image = TextureManager.get(image_path, self.size)
        else:
            self._image = TextureManager.get(image_path)
            image_width = self._image.get_width()
            image_height = self._image.get_height()

            container_ratio = self._width / self._height
            image_ratio = image_width / image_height

            limiting_container_side = self._height if container_ratio > image_ratio else self._width
            limiting_image_side = image_height if container_ratio > image_ratio else image_width
            factor = limiting_container_side / limiting_image_side

            new_width = int(image_width * factor)
            new_height = int(image_height * factor)

            self._image = pygame.transform.scale(self._image, (new_width, new_height))

        self._surface.blit(self._image, (0, 0))
        return self

    def set_size(self, width: int, height: int) -> Self:
        self._width = width
        self._height = height
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(self._background_color)
        self._draw_border()
        if self._child:
            self.update_child_position()
        return self

    def fit_to_image(self) -> Self:
        if self._image is None:
            return self
        return self.set_size(*self._image.get_size())

    def on_any_event(self, event: Event) -> None:
        if self._child is not None:
            self._child.on_any_event(event)

    def render(self, window: pygame.Surface) -> None:
        if self._image:
            self._surface.blit(self._image, (0, 0))

        window.blit(self._surface, self._position)

        if self._child:
            self._child.render(window)

    def _draw_border(self) -> None:
        rect_image = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(rect_image, (255, 255, 255), (0, 0, *self.size), border_radius=self._corner_radius)

        self._surface = self._surface.copy().convert_alpha()
        self._surface.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        if self._border_width != 0:
            pygame.draw.rect(
                self._surface,
                self._border_color,
                self._surface.get_rect(),
                self._border_width,
                self._corner_radius
            )
