import pygame

from events.event_type import EventType
from events.key_event import KeyEvent
from events.quit_event import QuitEvent

type Event = KeyEvent | QuitEvent | pygame.event.Event
