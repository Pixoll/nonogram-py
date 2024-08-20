from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class JoyBallMotionEvent:
    type: Literal[EventType.JOY_BALL_MOTION]
    """
    EventType.JOY_BALL_MOTION
    """

    instance_id: int
    """
    The joystick instance id
    """

    ball: int
    """
    The joystick trackball index
    """

    rel: int
    """
    The relative motion
    """

    def __init__(self, event: Event):
        self.type = EventType.JOY_BALL_MOTION
        self.instance_id = event.instance_id
        self.ball = event.ball
        self.rel = event.rel

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
