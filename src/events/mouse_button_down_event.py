from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class MouseButtonDownEvent:
    type: Literal[EventType.MOUSE_BUTTON_DOWN]
    pos: Any
    button: Any
    touch: Any

    def __init__(self, event: Event):
        self.type = EventType.MOUSE_BUTTON_DOWN
        self.pos = event.pos
        self.button = event.button
        self.touch = event.touch

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
