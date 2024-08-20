from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class RenderDeviceResetEvent:
    type: Literal[EventType.RENDER_DEVICE_RESET]

    def __init__(self, event: Event):
        self.type = EventType.RENDER_DEVICE_RESET

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
