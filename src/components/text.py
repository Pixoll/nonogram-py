from typing import Self

import pygame
from pygame.font import Font

from components.element import Element
from events import Event


class Text(Element):
    _text: str
    _font: Font
    _color: tuple[int, int, int]
    _text_surface: pygame.Surface

    def __init__(self, text: str, font: Font, color: tuple[int, int, int]):
        text_surface = font.render(text, True, color)
        super().__init__(*text_surface.get_size())

        self._text = text
        self._font = font
        self._color = color
        self._text_surface = text_surface

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def set_text(self, text: str) -> Self:
        self._text = text
        self._text_surface = self._font.render(self._text, True, self._color)
        self._width, self._height = self._text_surface.get_size()
        return self

    def set_color(self, color: tuple[int, int, int]) -> Self:
        self._color = color
        self._text_surface = self._font.render(self._text, True, self._color)
        return self

    def set_font(self, font: Font) -> Self:
        self._font = font
        self._text_surface = self._font.render(self._text, True, self._color)
        self._width, self._height = self._text_surface.get_size()
        return self

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window) -> None:
        window.blit(self._text_surface, self._position)
