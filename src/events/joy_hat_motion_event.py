from enum import Enum
from typing import Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class JoyHat(Enum):
    CENTERED = pygame.HAT_CENTERED
    DOWN = pygame.HAT_DOWN
    LEFT = pygame.HAT_LEFT
    LEFT_DOWN = pygame.HAT_LEFTDOWN
    LEFT_UP = pygame.HAT_LEFTUP
    RIGHT = pygame.HAT_RIGHT
    RIGHT_DOWN = pygame.HAT_RIGHTDOWN
    RIGHT_UP = pygame.HAT_RIGHTUP
    UP = pygame.HAT_UP


class JoyHatMotionEvent:
    type: Literal[EventType.JOY_HAT_MOTION]
    """
    EventType.JOY_HAT_MOTION
    """

    instance_id: int
    """
    The joystick instance id
    """

    hat: JoyHat
    """
    The joystick hat
    """

    value: tuple[int, int]
    """
    The hat position value
    """

    def __init__(self, event: Event):
        self.type = EventType.JOY_HAT_MOTION
        self.instance_id = event.instance_id
        self.hat = JoyHat(event.hat)
        self.value = event.value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
