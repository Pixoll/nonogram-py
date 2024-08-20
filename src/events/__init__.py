import pygame

from src.events.event_type import EventType
from src.events.key_event import KeyEvent
from src.events.quit_event import QuitEvent

type Event = KeyEvent | QuitEvent | pygame.event.Event
