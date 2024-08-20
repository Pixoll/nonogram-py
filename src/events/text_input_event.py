from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class TextInputEvent:
    type: Literal[EventType.TEXT_INPUT]
    text: Any

    def __init__(self, event: Event):
        self.type = EventType.TEXT_INPUT
        self.text = event.text

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
