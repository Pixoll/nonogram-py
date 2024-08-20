from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class ControllerDeviceRemappedEvent:
    type: Literal[EventType.CONTROLLER_DEVICE_REMAPPED]
    instance_id: Any

    def __init__(self, event: Event):
        self.type = EventType.CONTROLLER_DEVICE_REMAPPED
        self.instance_id = event.instance_id

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
