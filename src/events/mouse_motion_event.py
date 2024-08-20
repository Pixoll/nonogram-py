from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class MouseMotionEvent:
    type: Literal[EventType.MOUSE_MOTION]
    pos: Any
    rel: Any
    buttons: Any
    touch: Any

    def __init__(self, event: Event):
        self.type = EventType.MOUSE_MOTION
        self.pos = event.pos
        self.rel = event.rel
        self.buttons = event.buttons
        self.touch = event.touch

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
