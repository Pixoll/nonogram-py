from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class WindowEvent:
    type: (Literal[EventType.WINDOW_CLOSE]
           | Literal[EventType.WINDOW_CLOSE]
           | Literal[EventType.WINDOW_DISPLAY_CHANGED]
           | Literal[EventType.WINDOW_ENTER]
           | Literal[EventType.WINDOW_EXPOSED]
           | Literal[EventType.WINDOW_FOCUS_GAINED]
           | Literal[EventType.WINDOW_FOCUS_LOST]
           | Literal[EventType.WINDOW_HIDDEN]
           | Literal[EventType.WINDOW_HIT_TEST]
           | Literal[EventType.WINDOW_ICC_PROFILE_CHANGED]
           | Literal[EventType.WINDOW_LEAVE]
           | Literal[EventType.WINDOW_MAXIMIZED]
           | Literal[EventType.WINDOW_MINIMIZED]
           | Literal[EventType.WINDOW_MOVED]
           | Literal[EventType.WINDOW_RESIZED]
           | Literal[EventType.WINDOW_RESTORED]
           | Literal[EventType.WINDOW_SHOWN]
           | Literal[EventType.WINDOW_SIZE_CHANGED]
           | Literal[EventType.WINDOW_TAKE_FOCUS])

    def __init__(self, event: Event):
        self.type = EventType(event.type)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
