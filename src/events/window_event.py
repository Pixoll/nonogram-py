from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class WindowEvent:
    type: Literal[
        EventType.WINDOW_CLOSE,
        EventType.WINDOW_CLOSE,
        EventType.WINDOW_DISPLAY_CHANGED,
        EventType.WINDOW_ENTER,
        EventType.WINDOW_EXPOSED,
        EventType.WINDOW_FOCUS_GAINED,
        EventType.WINDOW_FOCUS_LOST,
        EventType.WINDOW_HIDDEN,
        EventType.WINDOW_HIT_TEST,
        EventType.WINDOW_ICC_PROFILE_CHANGED,
        EventType.WINDOW_LEAVE,
        EventType.WINDOW_MAXIMIZED,
        EventType.WINDOW_MINIMIZED,
        EventType.WINDOW_MOVED,
        EventType.WINDOW_RESIZED,
        EventType.WINDOW_RESTORED,
        EventType.WINDOW_SHOWN,
        EventType.WINDOW_SIZE_CHANGED,
        EventType.WINDOW_TAKE_FOCUS,
    ]
    """
    EventType.WINDOW_*
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
