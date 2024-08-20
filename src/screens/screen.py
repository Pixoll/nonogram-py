from abc import ABC, abstractmethod

from events import Event, KeyEvent, QuitEvent


class Screen(ABC):
    @abstractmethod
    def on_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    @abstractmethod
    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
