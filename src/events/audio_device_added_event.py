from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class AudioDeviceAddedEvent:
    type: Literal[EventType.AUDIO_DEVICE_ADDED]
    which: Any
    iscapture: Any

    def __init__(self, event: Event):
        self.type = EventType.AUDIO_DEVICE_ADDED
        self.which = event.which
        self.iscapture = event.iscapture

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
