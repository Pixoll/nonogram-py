from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class MouseWheelEvent:
    type: Literal[EventType.MOUSE_WHEEL]
    which: Any
    flipped: Any
    x: Any
    y: Any
    touch: Any
    precise_x: Any
    precise_y: Any

    def __init__(self, event: Event):
        self.type = EventType.MOUSE_WHEEL
        self.which = event.which
        self.flipped = event.flipped
        self.x = event.x
        self.y = event.y
        self.touch = event.touch
        self.precise_x = event.precise_x
        self.precise_y = event.precise_y

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
