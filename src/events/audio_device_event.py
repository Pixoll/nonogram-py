from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class AudioDeviceEvent:
    type: Literal[EventType.AUDIO_DEVICE_ADDED, EventType.AUDIO_DEVICE_REMOVED]
    """
    Either EventType.AUDIO_DEVICE_ADDED or EventType.AUDIO_DEVICE_REMOVED
    """

    which: int
    """
    The audio device index for the ADDED event
    
    Audio device id for the REMOVED event
    """

    is_capture: int
    """
    Zero if an output device, non-zero if a capture device
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.which = event.which
        self.is_capture = event.iscapture

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
