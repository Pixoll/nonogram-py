from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class VideoResizeEvent:
    type: Literal[EventType.VIDEO_RESIZE]
    size: Any
    w: Any
    h: Any

    def __init__(self, event: Event):
        self.type = EventType.VIDEO_RESIZE
        self.size = event.size
        self.w = event.w
        self.h = event.h

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
