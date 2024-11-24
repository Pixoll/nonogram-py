from typing import Self

import pygame
from pygame.font import Font

from components.element import Element
from events import Event, EventType, Key, MouseButton


class TextField(Element):
    _text: str
    _message: str
    _font: Font
    _color: tuple[int, int, int]
    _active_color: tuple[int, int, int]
    _inactive_color: tuple[int, int, int]
    _text_surface: pygame.Surface
    _active: bool
    _max_width: int
    _empty: bool

    def __init__(
            self,
            text: str,
            font: Font,
            inactive_color: tuple[int, int, int],
            active_color: tuple[int, int, int],
            max_width: int
    ):
        text_surface = font.render(text, True, inactive_color)
        super().__init__(*text_surface.get_size())
        self._message = text
        self._text = ""
        self._font = font
        self._color = inactive_color
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._text_surface = text_surface
        self._active = False
        self._max_width = max_width
        self._empty = True

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def set_text(self, text: str) -> Self:
        self._text = text
        self._update_surface()
        return self

    def get_text(self) -> str:
        if self._text == self._message:
            return ""
        else:
            return self._text

    def set_active(self, active: bool) -> Self:
        if active:
            self._active = True
            self._color = self._active_color
            if self._empty:
                self._text = ""
        else:
            if self._text == "":
                self._empty = True
            self._active = False
            self._color = self._inactive_color
            if self._empty:
                self._text = self._message
        self._update_surface()
        return self

    def _update_surface(self) -> None:
        display_text = self._text if self._text or self._active else self._message
        self._text_surface = self._font.render(display_text, True, self._color)
        self._width, self._height = self._text_surface.get_size()

    def on_any_event(self, event: Event) -> None:
        if self._active and event.type == EventType.KEY_DOWN:
            self._empty = False
            if event.key == Key.BACKSPACE:
                self._text = self._text[:-1]
            elif event.key == Key.RETURN:
                self.set_active(False)
            else:
                if self._width <= self._max_width - 30:
                    self._text += event.unicode
            self._update_surface()

    def render(self, window) -> None:
        window.blit(self._text_surface, self._position)
