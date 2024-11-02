from typing import Self
import pygame
from components.element import Element
from events import Event, EventType, Key, MouseButton

class DimensionSelector(Element):
    _default_value: int
    _current_value: str
    _font: pygame.font.Font
    _color: tuple[int, int, int]
    _active_color: tuple[int, int, int]
    _inactive_color: tuple[int, int, int]
    _text_surface: pygame.Surface
    _active: bool
    _max_width: int
    _empty: bool
    _max_value: int = 100

    def __init__(
            self,
            default_value: int,
            font: pygame.font.Font,
            inactive_color: tuple[int, int, int],
            active_color: tuple[int, int, int],
            max_width: int
    ):
        text_surface = font.render(str(default_value), True, inactive_color)
        super().__init__(*text_surface.get_size())
        self._default_value = min(default_value, self._max_value)
        self._current_value = ""
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

    def set_value(self, value: int) -> Self:
        self._current_value = str(min(value, self._max_value))
        self._empty = False
        self._update_surface()
        return self

    def set_default_value(self, default_value: int) -> Self:
        self._default_value = min(default_value, self._max_value)
        if self._empty:
            self._update_surface()
        return self

    def get_value(self) -> int:
        return int(self._current_value) if self._current_value else self._default_value

    def get_default_value(self) -> int:
        return self._default_value

    def _update_surface(self) -> None:
        display_text = self._current_value if self._current_value or self._active else str(self._default_value)
        display_color = self._active_color if self._active else self._inactive_color
        self._text_surface = self._font.render(display_text, True, display_color)
        self._width, self._height = self._text_surface.get_size()

    def on_any_event(self, event: Event) -> None:
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            mouse_pos = pygame.mouse.get_pos()
            if self.contains(mouse_pos):
                self._active = True
                self._color = self._active_color
                if self._empty:
                    self._current_value = ""
            else:
                if self._current_value == "":
                    self._empty = True
                self._active = False
                self._color = self._inactive_color
            self._update_surface()

        if self._active and event.type == EventType.KEY_DOWN:
            if event.key == Key.BACKSPACE:
                self._current_value = self._current_value[:-1]
                self._empty = self._current_value == ""
            elif event.key == Key.RETURN:
                self._active = False
                self._color = self._inactive_color
                if self._current_value == "":
                    self._empty = True
            else:
                if event.unicode.isdigit() and self._width <= self._max_width - 30:
                    potential_value = int(self._current_value + event.unicode) if self._current_value else int(event.unicode)
                    if potential_value <= self._max_value:
                        self._current_value += event.unicode
                        self._empty = False
            self._update_surface()

    def render(self, window) -> None:
        window.blit(self._text_surface, self._position)
