from components.element import Element
import pygame
from events import Event, EventType, MouseButton


class ColorBlock(Element):
    _color: tuple[int, int, int] | tuple[int, int, int, int]
    _position: tuple[int, int]
    _surface: pygame.Surface
    _hint_value: int | None
    _font: pygame.font.Font

    def __init__(self, width: int, height: int, color: tuple[int, int, int] | tuple[int, int, int, int], font: pygame.font.Font = None) -> None:
        super().__init__(width, height)
        self._color = color
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(self._color)
        self._hint_value = None
        self._font = font if font else pygame.font.SysFont(None, 24)

    def set_position(self, position: tuple[int, int]) -> None:
        self._position = position

    def set_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> None:
        self._color = color
        self._surface.fill(color)

    @property
    def color(self) -> tuple[int, int, int] | tuple[int, int, int, int]:
        return self._color

    def on_all_events(self, event: Event) -> None:
        return

    def set_hint(self, hint: int) -> None:
        self._hint_value = hint

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._surface, self._position)
        if self._hint_value is not None:
            hint_text = self._font.render(str(self._hint_value), True, (0, 0, 0))
            text_rect = hint_text.get_rect(center=(self._position[0] + self._surface.get_width() // 2,
                                                   self._position[1] + self._surface.get_height() // 2))
            screen.blit(hint_text, text_rect)

