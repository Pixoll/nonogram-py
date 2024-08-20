from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class ControllerDeviceAddedEvent:
    type: Literal[EventType.CONTROLLER_DEVICE_ADDED]
    device_index: Any

    def __init__(self, event: Event):
        self.type = EventType.CONTROLLER_DEVICE_ADDED
        self.device_index = event.device_index

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
