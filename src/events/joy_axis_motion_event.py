from enum import Enum, auto
from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class JoyAxis(Enum):
    LEFT_X = 0
    LEFT_Y = auto()
    RIGHT_X = auto()
    RIGHT_Y = auto()
    TRIGGER_LEFT = auto()
    TRIGGER_RIGHT = auto()
    MAX = auto()


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
    The joystick axis index 
    """

    value: float
    """
    The axis value (range: -32768 to 32767)
    """

    def __init__(self, event: Event):
        self.type = EventType.JOY_AXIS_MOTION
        self.instance_id = event.instance_id
        self.axis = JoyAxis(event.axis)
        self.value = event.value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
