import pygame
from components import Element
from components.block_with_image import BlockWithImage
from typing import Self
from events import Event, EventType, MouseButton, MouseWheelEvent

GRAY = (197, 194, 197)

class ScrollBar(Element):
    _bar_left: BlockWithImage
    _bar_right: BlockWithImage

    def __init__(self, width: int, content_width: int):
        super().__init__(width, 20)
        self.x_axis = 0
        self.content_width = content_width
        self.change_x = 0

        bar_width = int((width - 40) / (content_width / (width * 1.0)))
        self.bar_rect = pygame.Rect(20, self._position[1], bar_width, 20)

        self._bar_left = BlockWithImage(20, 20, "left.png")
        self._bar_right = BlockWithImage(20, 20, "right.png")

        self.on_bar = False
        self.mouse_diff = 0

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._bar_left.set_position((position[0], position[1]))
        self._bar_right.set_position((position[0] + self._width - 20, position[1]))
        return self

    def update(self):
        self.x_axis += self.change_x

        if self.x_axis > 0:
            self.x_axis = 0
        elif (self.x_axis + self.content_width) < self._width:
            self.x_axis = self._width - self.content_width

        width_diff = self.content_width - self._width
        scroll_length = self._width - self.bar_rect.width - 40
        bar_half_length = self.bar_rect.width / 2 + 20

        if self.on_bar:
            pos = pygame.mouse.get_pos()
            self.bar_rect.x = pos[0] - self.mouse_diff
            if self.bar_rect.left < 20:
                self.bar_rect.left = 20
            elif self.bar_rect.right > (self._width - 20):
                self.bar_rect.right = self._width - 20

            self.x_axis = int(width_diff / (scroll_length * 1.0) * (self.bar_rect.centerx - bar_half_length) * -1)
        else:
            self.bar_rect.centerx = scroll_length / (width_diff * 1.0) * (self.x_axis * -1) + bar_half_length

    def on_all_events(self, event: Event) -> None:

        if event.type == EventType.MOUSE_WHEEL:
            wheel_event: MouseWheelEvent = event
            down = wheel_event.precise_y < 0 if wheel_event.flipped else wheel_event.precise_y > 0
            self.change_x = -5 if down else 5

        pos = pygame.mouse.get_pos()

        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            pos = pygame.mouse.get_pos()
            if self._bar_left.contains(pos):
                print("Presionó barra izquierda")
                self.change_x = 5
            elif self._bar_right.contains(pos):
                print("Presionó barra derecha")
                self.change_x = -5

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
        pygame.draw.rect(window, GRAY, self.bar_rect)
        self._bar_left.render(window)
        self._bar_right.render(window)

