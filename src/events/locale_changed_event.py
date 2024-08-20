from typing import Literal

from events.event_type import EventType


class LocaleChangedEvent:
    type: Literal[EventType.LOCALE_CHANGED]
    """
    EventType.LOCALE_CHANGED
    """

    def __init__(self):
        self.type = EventType.LOCALE_CHANGED

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
