from typing import Self

import pygame

from components.element import Element
from events import Event


class ColoredBlock(Element):
    _color: tuple[int, int, int]
    _position: tuple[int, int]
    _surface: pygame.Surface
    _text: str | None
    _font: pygame.font.Font | None
    _text_color: tuple[int, int, int]

    def __init__(
            self,
            size: int,
            color: tuple[int, int, int],
            text: str | None = None,
            font: pygame.font.Font | None = None
    ) -> None:
        super().__init__(size, size)
        self._color = color
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._surface.fill(self._color)
        self._text = text
        self._font = font
        self._text_color = self._calculate_text_color()
        self._selected = False
        self._border_color = (255, 255, 255)  # Initial border is white

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def set_color(self, color: tuple[int, int, int]) -> Self:
        self._color = color
        self._surface.fill(color)
        self._text_color = self._calculate_text_color()
        return self

    def set_text(self, text: str) -> Self:
        self._text = text
        return self

    def change_state(self) -> None:
        self._selected = not self._selected

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    def on_any_event(self, event: Event) -> None:
        return

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._surface, self._position)

        if self._selected:
            pygame.draw.rect(
                screen,
                self._border_color,
                (self._position[0], self._position[1], self.size[0], self.size[1]),
                2  # Border thickness
            )

        if self._text is not None and self._font is not None:
            block_text = self._font.render(self._text, True, self._text_color)
            text_rect = block_text.get_rect(center=(self._position[0] + self._surface.get_width() // 2,
                                                    self._position[1] + self._surface.get_height() // 2))
            screen.blit(block_text, text_rect)

    def _calculate_text_color(self) -> tuple[int, int, int]:
        r, g, b = self._color
        luminance = r * 0.2126 + g * 0.7152 + b * 0.0722
        return (255, 255, 255) if luminance < 140 else (0, 0, 0)
