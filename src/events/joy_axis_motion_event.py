from enum import Enum
from typing import Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class JoyAxis(Enum):
    INVALID = pygame.CONTROLLER_AXIS_INVALID
    LEFT_X = pygame.CONTROLLER_AXIS_LEFTX
    LEFT_Y = pygame.CONTROLLER_AXIS_LEFTY
    RIGHT_X = pygame.CONTROLLER_AXIS_RIGHTX
    RIGHT_Y = pygame.CONTROLLER_AXIS_RIGHTY
    TRIGGER_LEFT = pygame.CONTROLLER_AXIS_TRIGGERLEFT
    TRIGGER_RIGHT = pygame.CONTROLLER_AXIS_TRIGGERRIGHT
    MAX = pygame.CONTROLLER_AXIS_MAX


class JoyAxisMotionEvent:
    type: Literal[EventType.JOY_AXIS_MOTION]
    """
    EventType.JOY_AXIS_MOTION
    """

    instance_id: int
    """
    The joystick instance id
    """

    axis: JoyAxis
    """
    The joystick axis 
    """

    value: float
    """
    The axis value (range: -1.0 to 1.0)
    """

    def __init__(self, event: Event):
        self.type = EventType.JOY_AXIS_MOTION
        self.instance_id = event.instance_id
        self.axis = JoyAxis(event.axis)
        self.value = event.value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
