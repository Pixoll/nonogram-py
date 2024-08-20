from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class JoyDeviceEvent:
    type: Literal[EventType.JOY_DEVICE_ADDED] | Literal[EventType.JOY_DEVICE_REMOVED]
    """
    Either EventType.JOY_DEVICE_ADDED or EventType.JOY_DEVICE_REMOVED
    """

    which: int
    """
    The joystick device index for the ADDED event, instance id for the REMOVED event
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.which = event.device_index if self.type == EventType.JOY_DEVICE_ADDED else event.instance_id

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
