from abc import ABC, abstractmethod

from events import Event, KeyEvent, MouseButtonEvent, MouseMotionEvent, QuitEvent


class Screen(ABC):
    @abstractmethod
    def on_any_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def on_key_event(self, event: KeyEvent) -> None:
        pass

    @abstractmethod
    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        pass

    @abstractmethod
    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    @abstractmethod
    def on_quit_event(self, event: QuitEvent) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
