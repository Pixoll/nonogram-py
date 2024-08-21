from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class VideoResizeEvent:
    type: Literal[EventType.VIDEO_RESIZE]
    """
    EventType.VIDEO_RESIZE
    """

    w: int
    """
    New video width
    """

    h: int
    """
    New video height
    """

    def __init__(self, event: Event):
        self.type = EventType.VIDEO_RESIZE
        self.w = event.w
        self.h = event.h

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
