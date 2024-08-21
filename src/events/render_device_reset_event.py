from typing import Literal

from events.event_type import EventType


class RenderDeviceResetEvent:
    type: Literal[EventType.RENDER_DEVICE_RESET]
    """
    EventType.RENDER_DEVICE_RESET
    """

    def __init__(self):
        self.type = EventType.RENDER_DEVICE_RESET

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
