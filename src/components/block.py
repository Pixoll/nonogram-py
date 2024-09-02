from enum import Enum
from typing import Self, Literal

import pygame

from components.element_with_child import ElementWithChild
from events import Event, EventType, MouseButton


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

        self._x_image = pygame.transform.scale(pygame.image.load('assets/textures/x.gif'), self.size)

    def set_background_color(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> Self:
        self._background_color = color
        self._surface.fill(self._background_color)
        return self

    def set_position(self, new_position: tuple[int, int]) -> Self:
        self._position = new_position
        self._update_child_position()
        return self

    def set_state(self, state: State) -> None:
        if state == Block.State.COLORED:
            if self._state == Block.State.COLORED:
                self._state = Block.State.EMPTY
                self.set_background_color((255, 255, 255))
            else:
                if self._state == Block.State.CROSSED:
                    self.toggle_x_mark()
                self._state = Block.State.COLORED
                self.set_background_color((0, 0, 0))

            return

        if self._state == Block.State.CROSSED:
            self.toggle_x_mark()
            self._state = Block.State.EMPTY
            self.set_background_color((255, 255, 255))
        else:
            self._state = Block.State.CROSSED
            self.set_background_color((255, 255, 255))
            self.toggle_x_mark()

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN:
            return

        if event.button != MouseButton.LEFT and event.button != MouseButton.RIGHT:
            return

        if self.contains(pygame.mouse.get_pos()):
            self.set_state(Block.State(int(event.button == MouseButton.LEFT)))

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
