from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class DropStatusEvent:
    type: Literal[EventType.DROP_BEGIN, EventType.DROP_COMPLETE]
    """
    Either EventType.DROP_BEGIN or EventType.DROP_COMPLETE
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
