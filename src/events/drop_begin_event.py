from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class DropBeginEvent:
    type: Literal[EventType.DROP_BEGIN]

    def __init__(self, event: Event):
        self.type = EventType.DROP_BEGIN

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
