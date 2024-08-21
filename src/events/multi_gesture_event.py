from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class MultiGestureEvent:
    type: Literal[EventType.MULTI_GESTURE]
    """
    EventType.MULTI_GESTURE
    """

    touch_id: int
    """
    The touch device id
    """

    x: float
    y: float
    pinched: Any
    rotated: Any
    num_fingers: int

    def __init__(self, event: Event):
        self.type = EventType.MULTI_GESTURE
        self.touch_id = event.touch_id
        self.x = event.x
        self.y = event.y
        self.pinched = event.pinched
        self.rotated = event.rotated
        self.num_fingers = event.num_fingers

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
