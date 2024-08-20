import pygame

from events import QuitEvent, KeyEvent, EventType
from src.events import Event
from src.screens.screen import Screen


class Engine:
    screen: Screen

    def __init__(self):
        pass

    def set_screen(self, screen: Screen) -> None:
        self.screen = screen

    def run(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        if not hasattr(self, "screen"):
            raise Exception("No screen")

        running = True

        while running:
            for raw_event in pygame.event.get():
                event = Engine._parse_event(raw_event)
                print(event)

                self.screen.on_event(event)

                if event.type == EventType.QUIT:
                    running = False

            window.fill("purple")
            self.screen.render()
            pygame.display.flip()

            clock.tick(60)

    @staticmethod
    def _parse_event(event: pygame.event.Event) -> Event:
        match event.type:
            case pygame.QUIT:
                return QuitEvent()
            case pygame.KEYDOWN | pygame.KEYUP:
                return KeyEvent(event)
            case _:
                return event
