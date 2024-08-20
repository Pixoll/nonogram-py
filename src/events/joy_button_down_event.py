from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class JoyButtonDownEvent:
    type: Literal[EventType.JOY_BUTTON_DOWN]
    instance_id: Any
    button: Any

    def __init__(self, event: Event):
        self.type = EventType.JOY_BUTTON_DOWN
        self.instance_id = event.instance_id
        self.button = event.button

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
