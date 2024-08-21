from typing import Literal

from events.event_type import EventType


class RenderTargetsResetEvent:
    type: Literal[EventType.RENDER_TARGETS_RESET]
    """
    EventType.RENDER_TARGETS_RESET
    """

    def __init__(self):
        self.type = EventType.RENDER_TARGETS_RESET

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
