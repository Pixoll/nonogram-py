from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class TextEditingEvent:
    type: Literal[EventType.TEXT_EDITING]
    """
    EventType.TEXT_EDITING
    """

    text: str
    """
    The editing text
    """

    start: int
    """
    The start cursor of selected editing text
    """

    length: int
    """
    The length of selected editing text
    """

    def __init__(self, event: Event):
        self.type = EventType.TEXT_EDITING
        self.text = event.text
        self.start = event.start
        self.length = event.length

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
