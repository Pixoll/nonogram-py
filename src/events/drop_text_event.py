from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class DropTextEvent:
    type: Literal[EventType.DROP_TEXT]
    text: Any

    def __init__(self, event: Event):
        self.type = EventType.DROP_TEXT
        self.text = event.text

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
