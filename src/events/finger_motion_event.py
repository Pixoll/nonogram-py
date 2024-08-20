from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class FingerMotionEvent:
    type: Literal[EventType.FINGER_MOTION]
    touch_id: Any
    finger_id: Any
    x: Any
    y: Any
    dx: Any
    dy: Any

    def __init__(self, event: Event):
        self.type = EventType.FINGER_MOTION
        self.touch_id = event.touch_id
        self.finger_id = event.finger_id
        self.x = event.x
        self.y = event.y
        self.dx = event.dx
        self.dy = event.dy

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
