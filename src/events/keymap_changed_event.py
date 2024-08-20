from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class KeymapChangedEvent:
    type: Literal[EventType.KEYMAP_CHANGED]

    def __init__(self, event: Event):
        self.type = EventType.KEYMAP_CHANGED

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
