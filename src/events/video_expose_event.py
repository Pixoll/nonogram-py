from typing import Literal

from events.event_type import EventType


class VideoExposeEvent:
    type: Literal[EventType.VIDEO_EXPOSE]
    """
    EventType.VIDEO_EXPOSE
    """

    def __init__(self):
        self.type = EventType.VIDEO_EXPOSE

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
