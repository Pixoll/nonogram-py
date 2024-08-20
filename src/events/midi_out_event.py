from typing import Any, Literal

from pygame.event import Event

from events.event_type import EventType


class MidiOutEvent:
    type: Literal[EventType.MIDI_OUT]

    def __init__(self, event: Event):
        self.type = EventType.MIDI_OUT

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
