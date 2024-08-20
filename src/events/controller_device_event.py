from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class ControllerDeviceEvent:
    type: (Literal[EventType.CONTROLLER_DEVICE_ADDED]
           | Literal[EventType.CONTROLLER_DEVICE_REMAPPED]
           | Literal[EventType.CONTROLLER_DEVICE_REMOVED])
    """
    Either EventType.CONTROLLER_DEVICE_ADDED, EventType.CONTROLLER_DEVICE_REMAPPED
    or EventType.CONTROLLER_DEVICE_REMOVED
    """

    which: int
    """
    The controller device index for the ADDED event, instance id for the REMOVED or REMAPPED event
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.which = event.device_index if self.type == EventType.CONTROLLER_DEVICE_ADDED else event.instance_id

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
