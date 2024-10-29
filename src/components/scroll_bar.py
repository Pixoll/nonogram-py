from typing import Self

import pygame

from components import Element
from components.block_with_image import BlockWithImage
from events import Event, EventType, MouseButton

GRAY = (197, 194, 197)


class ScrollBar(Element):
    _bar_left: BlockWithImage
    _bar_right: BlockWithImage
    _bar: BlockWithImage

    def __init__(self, width: int, content_width: int):
        super().__init__(width, 20)
        self.x_axis = 0
        self.content_width = content_width
        self.change_x = 0

        bar_width = int((width - 40) * (width / content_width))

        self._bar_left = BlockWithImage(20, 20, "left.png")
        self._bar_right = BlockWithImage(20, 20, "right.png")
        self._bar = BlockWithImage(bar_width, 20, "bar.png")

        self.on_bar = False
        self.mouse_diff = 0

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._bar_left.set_position((position[0], position[1]))
        self._bar_right.set_position((position[0] + self._width - 20, position[1]))
        self._bar.set_position((position[0] + 20, position[1]))
        return self

    def update(self):
        self.x_axis += self.change_x

        if self.x_axis > 0:
            self.x_axis = 0
        elif (self.x_axis + self.content_width) < self._width:
            self.x_axis = self._width - self.content_width

        width_diff = self.content_width - self._width
        scroll_length = self._width - self._bar.size[0] - 40
        bar_half_length = self._bar.size[0] / 2 + 20

        if self.on_bar:
            pos = pygame.mouse.get_pos()
            self._bar.set_position((pos[0] - self.mouse_diff, self._position[1]))

            if self._bar.position[0] < 20:
                self._bar.set_position((20, self._position[1]))
            elif self._bar.position[0] + self._bar.size[0] > self._width - 20:
                self._bar.set_position((self._width - self._bar.size[0] - 20, self._position[1]))

            self.x_axis = int(width_diff / scroll_length * (self._bar.position[0] - bar_half_length) * -1)

    def on_all_events(self, event: Event) -> None:
        pos = pygame.mouse.get_pos()

        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            if self._bar_left.contains(pos):
                self.change_x = 5
            elif self._bar_right.contains(pos):
                self.change_x = -5
            elif self._bar.contains(pos):
                self.on_bar = True
                self.mouse_diff = pos[0] - self._bar.position[0]

        if event.type == EventType.MOUSE_BUTTON_UP and event.button == MouseButton.LEFT:
            self.change_x = 0
            self.on_bar = False

        if event.type == EventType.KEY_DOWN:
            if event.key == pygame.K_LEFT:
                self.change_x = 5
            elif event.key == pygame.K_RIGHT:
                self.change_x = -5

        if event.type == EventType.KEY_UP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.change_x = 0

    def render(self, window: pygame.Surface) -> None:
        self.update()
        self._bar.render(window)
        self._bar_left.render(window)
        self._bar_right.render(window)
