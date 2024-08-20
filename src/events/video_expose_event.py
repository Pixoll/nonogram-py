from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class VideoExposeEvent:
    type: Literal[EventType.VIDEO_EXPOSE]

    def __init__(self, event: Event):
        self.type = EventType.VIDEO_EXPOSE

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
