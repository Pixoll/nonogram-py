from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class JoyButtonEvent:
    type: Literal[EventType.JOY_BUTTON_DOWN] | Literal[EventType.JOY_BUTTON_UP]
    """
    Either EventType.JOY_BUTTON_DOWN or EventType.JOY_BUTTON_UP
    """

    instance_id: int
    """
    The joystick instance id
    """

    button: int
    """
    The joystick button index
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.instance_id = event.instance_id
        self.button = event.button

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
