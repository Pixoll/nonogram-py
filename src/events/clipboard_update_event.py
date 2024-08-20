from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class ClipboardUpdateEvent:
    type: Literal[EventType.CLIPBOARD_UPDATE]

    def __init__(self, event: Event):
        self.type = EventType.CLIPBOARD_UPDATE

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
