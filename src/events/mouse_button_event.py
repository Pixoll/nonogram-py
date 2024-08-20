from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class MouseButtonEvent:
    type: Literal[EventType.MOUSE_BUTTON_DOWN] | Literal[EventType.MOUSE_BUTTON_UP]
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

    button: int
    """
    The mouse button index
    """

    touch: bool
    """
    Whether or not the event was generated by a touch input device
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.x = event.pos[0]
        self.y = event.pos[1]
        self.button = event.button
        self.touch = event.touch

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
