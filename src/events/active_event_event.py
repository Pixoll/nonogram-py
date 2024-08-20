from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class ActiveEventEvent:
    type: Literal[EventType.ACTIVE_EVENT]
    gain: Any
    state: Any

    def __init__(self, event: Event):
        self.type = EventType.ACTIVE_EVENT
        self.gain = event.gain
        self.state = event.state

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
