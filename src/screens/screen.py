from abc import ABC, abstractmethod

from pygame.event import Event


class Screen(ABC):
    @abstractmethod
    def run_logic(self, event: Event) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
