from enum import Enum
from typing import Literal

import pygame
from pygame.event import Event

from events.event_type import EventType


class JoyButton(Enum):
    A = pygame.CONTROLLER_BUTTON_A
    B = pygame.CONTROLLER_BUTTON_B
    X = pygame.CONTROLLER_BUTTON_X
    Y = pygame.CONTROLLER_BUTTON_Y
    BACK = pygame.CONTROLLER_BUTTON_BACK
    GUIDE = pygame.CONTROLLER_BUTTON_GUIDE
    START = pygame.CONTROLLER_BUTTON_START
    LEFT_STICK = pygame.CONTROLLER_BUTTON_LEFTSTICK
    RIGHT_STICK = pygame.CONTROLLER_BUTTON_RIGHTSTICK
    LEFT_SHOULDER = pygame.CONTROLLER_BUTTON_LEFTSHOULDER
    RIGHT_SHOULDER = pygame.CONTROLLER_BUTTON_RIGHTSHOULDER
    DPAD_UP = pygame.CONTROLLER_BUTTON_DPAD_UP
    DPAD_DOWN = pygame.CONTROLLER_BUTTON_DPAD_DOWN
    DPAD_LEFT = pygame.CONTROLLER_BUTTON_DPAD_LEFT
    DPAD_RIGHT = pygame.CONTROLLER_BUTTON_DPAD_RIGHT
    MAX = pygame.CONTROLLER_BUTTON_MAX


class JoyButtonEvent:
    type: Literal[EventType.JOY_BUTTON_DOWN] | Literal[EventType.JOY_BUTTON_UP]
    """
    Either EventType.JOY_BUTTON_DOWN or EventType.JOY_BUTTON_UP
    """

    instance_id: int
    """
    The joystick instance id
    """

    button: JoyButton
    """
    The joystick button
    """

    def __init__(self, event: Event):
        self.type = EventType(event.type)
        self.instance_id = event.instance_id
        self.button = JoyButton(event.button)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
