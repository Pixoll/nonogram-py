from typing import Any, Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class JoyHatMotionEvent:
    type: Literal[EventType.JOY_HAT_MOTION]
    """
    EventType.JOY_HAT_MOTION
    """

    instance_id: int
    """
    The joystick instance id
    """

    hat: int
    """
    The joystick hat index
    """

    value: tuple[int, int]
    """
    The hat position value
    """

    def __init__(self, event: Event):
        self.type = EventType.JOY_HAT_MOTION
        self.instance_id = event.instance_id
        self.hat = event.hat
        self.value = event.value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
