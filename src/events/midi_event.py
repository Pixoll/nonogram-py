from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class MidiEvent:
    type: Literal[EventType.MIDI_IN, EventType.MIDI_OUT]
    """
    Either EventType.MIDI_IN or EventType.MIDI_OUT
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
