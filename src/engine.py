import pygame

from src.screens.screen import Screen


class Engine:
    screen: Screen

    def __init__(self):
        pass

    def set_screen(self, screen: Screen) -> None:
        self.screen = screen

    def run(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        running = True

        while running:
            for event in pygame.event.get():
                self.screen.on_event(event)

                if event.type == pygame.QUIT:
                    running = False

            window.fill("purple")
            self.screen.render()
            pygame.display.flip()

            clock.tick(60)
