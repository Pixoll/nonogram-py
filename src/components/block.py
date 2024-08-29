from typing import Self

import pygame

from components.element_with_child import ElementWithChild
from events import Event, EventType, MouseButton


class Block(ElementWithChild):
    _surface: pygame.Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_color: tuple[int, int, int] | tuple[int, int, int, int]
    _border_width: int
    _state: int
    _x_mark_visible: bool
    _x_image: pygame.Surface

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._surface = pygame.Surface(self.size)
        self._background_color = (255, 255, 255)
        self._border_color = (0, 0, 0)
        self._border_width = 1

        self._surface.fill(self._background_color)
        self._draw_border()

        self._state = 0
        self._x_mark_visible = False

        self._x_image = pygame.transform.scale(pygame.image.load('assets/textures/x.gif'), self.size)

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        self._draw_border()
        return self

    def set_border_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._border_color = color
        self._draw_border()
        return self

    def set_border_width(self, border_width: int) -> Self:
        self._border_width = border_width
        self._draw_border()
        return self

    def set_position(self, new_position: tuple[int, int]) -> Self:
        self._position = new_position
        self._update_child_position()
        return self

    def set_state(self, state: int) -> None:
        if state == 1:
            if self._state == 1:
                self._state = 0
                self.set_background_color((255, 255, 255))
            else:
                if self._state == 3:
                    self.toggle_x_mark()
                self._state = 1
                self.set_background_color((0, 0, 0))

            return

        if self._state == 3:
            self.toggle_x_mark()
            self._state = 0
            self.set_background_color((255, 255, 255))
        else:
            self._state = 3
            self.set_background_color((255, 255, 255))
            self.toggle_x_mark()

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if self.contains(pygame.mouse.get_pos()):
            self.set_state(int(event.button == MouseButton.LEFT))

    def render(self, window: pygame.Surface) -> None:
        window.blit(self._surface, self.position)
        if self._child:
            self._child.render(window)

    def toggle_x_mark(self) -> None:
        if self._x_mark_visible:
            self._surface.fill(self._background_color)
            self._draw_border()
            self._x_mark_visible = False
            return

        x_center = (self._surface.get_width() - self._x_image.get_width()) // 2
        y_center = (self._surface.get_height() - self._x_image.get_height()) // 2
        self._surface.blit(self._x_image, (x_center, y_center))
        self._draw_border()
        self._x_mark_visible = True

    def _draw_border(self) -> None:
        pygame.draw.rect(self._surface, self._border_color, self._surface.get_rect(), self._border_width)
