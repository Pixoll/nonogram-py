from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class DropFileEvent:
    type: Literal[EventType.DROP_FILE]
    """
    EventType.DROP_FILE
    """

    file: str
    """
    Path of the dropped file
    """

    def __init__(self, event: Event):
        self.type = EventType.DROP_FILE
        self.file = event.file

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
