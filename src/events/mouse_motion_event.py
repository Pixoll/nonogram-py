from typing import Literal

from pygame.event import Event

from events.event_type import EventType


class MouseMotionEvent:
    type: Literal[EventType.MOUSE_MOTION]
    """
    EventType.MOUSE_MOTION
    """

    x: int
    """
    X coordinate, relative to window
    """

    y: int
    """
    Y coordinate, relative to window
    """

    rel_x: int
    """
    The relative motion in the X direction
    """

    rel_y: int
    """
    The relative motion in the Y direction
    """

    left_button: bool
    """
    Whether the left mouse button was pressed
    """

    middle_button: bool
    """
    Whether the middle mouse button was pressed
    """

    right_button: bool
    """
    Whether the right mouse button was pressed
    """

    touch: bool
    """
    Whether or not the event was generated by a touch input device
    """

    def __init__(self, event: Event):
        self.type = EventType.MOUSE_MOTION
        self.x, self.y = event.pos
        self.rel_x, self.rel_y = event.rel
        self.left_button, self.middle_button, self.right_button = (bool(x) for x in event.buttons)
        self.touch = event.touch

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
