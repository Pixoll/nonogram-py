from typing import Self
import pygame
from components.element import Element
from events import Event, EventType, MouseButton, Key


class TextField(Element):
    _text: str
    _font: pygame.font.Font
    _color: tuple[int, int, int]
    _active_color: tuple[int, int, int]
    _inactive_color: tuple[int, int, int]
    _text_surface: pygame.Surface
    _active: bool
    _max_width: int

    def __init__(self, text: str, font: pygame.font.Font, inactive_color: tuple[int, int, int], active_color: tuple[int, int, int], max_width: int):
        text_surface = font.render(text, True, inactive_color)
        super().__init__(*text_surface.get_size())

        self._text = text
        self._font = font
        self._color = inactive_color
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._text_surface = text_surface
        self._active = False
        self.max_width = max_width

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def set_text(self, text: str) -> Self:
        self._text = text
        self._text_surface = self._font.render(self._text, True, self._color)
        self._width, self._height = self._text_surface.get_size()
        return self

    def get_text(self) -> str:
        return self._text

    def _update_surface(self) -> None:
        self._text_surface = self._font.render(self._text, True, self._color)

    def on_all_events(self, event: Event) -> None:
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:

            mouse_pos = pygame.mouse.get_pos()
            if self.contains(mouse_pos):
                self._active = True
                self._color = self._active_color
            else:
                self._active = False
                self._color = self._inactive_color
            self._update_surface()

        if self._active and event.type == EventType.KEY_DOWN:
            if event.key == Key.BACKSPACE:
                self._text = self._text[:-1]
            elif event.key == Key.RETURN:
                self._active = False
                self._color = self._inactive_color
            else:
                if self._width <= self.max_width - 30:
                    self._text += event.unicode
            self._update_surface()
            self._height = self._text_surface.get_height()
            self._width = self._text_surface.get_width()

    def render(self, window) -> None:
        window.blit(self._text_surface, self._position)
