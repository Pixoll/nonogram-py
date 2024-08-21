from typing import Literal

from events.event_type import EventType


class KeymapChangedEvent:
    type: Literal[EventType.KEYMAP_CHANGED]
    """
    EventType.KEYMAP_CHANGED
    """

    def __init__(self):
        self.type = EventType.KEYMAP_CHANGED

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
