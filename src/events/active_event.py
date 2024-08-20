from enum import Enum
from typing import Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class State(Enum):
    APP_ACTIVE = pygame.APPACTIVE
    APP_INPUT_FOCUS = pygame.APPINPUTFOCUS
    APP_MOUSE_FOCUS = pygame.APPMOUSEFOCUS


class ActiveEvent:
    """
    **DEPRECATED**
    """

    type: Literal[EventType.ACTIVE_EVENT]
    """
    EventType.ACTIVE_EVENT
    """

    gain: bool
    state: State

    def __init__(self, event: Event):
        self.type = EventType.ACTIVE_EVENT
        self.gain = bool(event.gain)
        self.state = State(event.state)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
