from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class UserEvent:
    type: Literal[EventType.USER_EVENT]
    """
    EventType.USER_EVENT
    """

    code: int
    """
    User defined event code
    """

    def __init__(self, event: Event):
        self.type = EventType.USER_EVENT
        self.code = event.code

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
