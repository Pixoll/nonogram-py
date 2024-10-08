from enum import Enum
from typing import Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class MouseButton(Enum):
    LEFT = pygame.BUTTON_LEFT
    MIDDLE = pygame.BUTTON_MIDDLE
    RIGHT = pygame.BUTTON_RIGHT
    WHEEL_DOWN = pygame.BUTTON_WHEELDOWN
    WHEEL_UP = pygame.BUTTON_WHEELUP
    X1 = pygame.BUTTON_X1
    X2 = pygame.BUTTON_X2


class MouseButtonEvent:
    type: Literal[EventType.MOUSE_BUTTON_DOWN, EventType.MOUSE_BUTTON_UP]
    """
    Either EventType.MOUSE_BUTTON_DOWN or EventType.MOUSE_BUTTON_UP
    """

    x: int
    """
    X coordinate, relative to window
    """

    y: int
    """
    Y coordinate, relative to window
    """

    button: MouseButton
    """
    The mouse button
    """

    touch: bool
    """
    Whether or not the event was generated by a touch input device
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.x, self.y = event.pos
        self.button = MouseButton(event.button)
        self.touch = event.touch

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
