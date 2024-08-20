from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class JoyAxisMotionEvent:
    type: Literal[EventType.JOY_AXIS_MOTION]
    instance_id: Any
    axis: Any
    value: Any

    def __init__(self, event: Event):
        self.type = EventType.JOY_AXIS_MOTION
        self.instance_id = event.instance_id
        self.axis = event.axis
        self.value = event.value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
