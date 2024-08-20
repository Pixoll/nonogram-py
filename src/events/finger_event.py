from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class FingerEvent:
    type: Literal[EventType.FINGER_DOWN] | Literal[EventType.FINGER_MOTION] | Literal[EventType.FINGER_UP]
    """
    Either EventType.FINGER_DOWN, EventType.FINGER_MOTION or EventType.FINGER_UP
    """

    touch_id: int
    """
    The touch device id
    """

    finger_id: int
    """
    The finger id
    """

    x: float
    """
    The x-axis location of the touch event, normalized (0...1)
    """

    y: float
    """
    The y-axis location of the touch event, normalized (0...1)
    """

    dx: float
    """
    The distance moved in the x-axis, normalized (-1...1)
    """

    dy: float
    """
    The distance moved in the y-axis, normalized (-1...1)
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.touch_id = event.touch_id
        self.finger_id = event.finger_id
        self.x = event.x
        self.y = event.y
        self.dx = event.dx
        self.dy = event.dy

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
