from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class QuitEvent:
    type: Literal[EventType.QUIT]

    def __init__(self, event: Event):
        self.type = EventType.QUIT

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
