from enum import Enum
from typing import Literal, Self

import pygame

from components.element_with_child import ElementWithChild
from events import Event


class Block(ElementWithChild):
    class State(Enum):
        EMPTY = 0
        COLORED = 1
        CROSSED = 2

    _surface: pygame.Surface
    _background_color: tuple[int, int, int] | tuple[int, int, int, int]
    _state: State
    _x_mark_visible: bool
    _x_image: pygame.Surface

    def __init__(self, width: int, height: int, color: tuple[int, int, int] | Literal["x"] | None):
        super().__init__(width, height)
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self._background_color = color if type(color) is tuple else (255, 255, 255)

        self._surface.fill(self._background_color)

        self._state = Block.State.EMPTY
        self._x_mark_visible = color == "x"

        self._x_image = pygame.transform.scale(pygame.image.load("assets/textures/x.gif"), self.size)

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        return self

    def set_position(self, new_position: tuple[int, int]) -> Self:
        self._position = new_position
        self._update_child_position()
        return self

    def set_state(self, new_state: State, color: tuple[int, int, int] | None) -> None:
        if new_state == Block.State.COLORED:
            if self._state == Block.State.COLORED:
                if color is not None and self._background_color != color:
                    self.set_background_color(color)
                else:
                    self._state = Block.State.EMPTY
                    self.set_background_color((255, 255, 255))
            else:
                if self._state == Block.State.CROSSED:
                    self.toggle_x_mark()
                self._state = Block.State.COLORED
                self.set_background_color(color)

            return

        if self._state == Block.State.CROSSED:
            self.toggle_x_mark()
            self._state = Block.State.EMPTY
            self.set_background_color((255, 255, 255))
        else:
            self._state = Block.State.CROSSED
            self.set_background_color((255, 255, 255))
            self.toggle_x_mark()

    @property
    def color(self) -> tuple[int, int, int]:
        return self._background_color

    @property
    def state(self) -> State:
        return self._state

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window: pygame.Surface) -> None:
        window.blit(self._surface, self.position)
        if self._child:
            self._child.render(window)

    def toggle_x_mark(self) -> None:
        if self._x_mark_visible:
            self._surface.fill(self._background_color)
            self._x_mark_visible = False
            return

        x_center = (self._surface.get_width() - self._x_image.get_width()) // 2
        y_center = (self._surface.get_height() - self._x_image.get_height()) // 2
        self._surface.blit(self._x_image, (x_center, y_center))
        self._x_mark_visible = True
