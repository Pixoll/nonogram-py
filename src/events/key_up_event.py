from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class KeyUpEvent:
    type: Literal[EventType.KEY_UP]
    key: Any
    mod: Any
    unicode: Any
    scancode: Any

    def __init__(self, event: Event):
        self.type = EventType.KEY_UP
        self.key = event.key
        self.mod = event.mod
        self.unicode = event.unicode
        self.scancode = event.scancode

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
