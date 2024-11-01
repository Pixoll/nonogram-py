import pygame

from assets import FontManager
from components import ChildAlignment, Container, Text
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class SettingsScreen(Screen):
    _engine: Engine
    _menu: Container
    _button: Container

    def __init__(self, engine: Engine):
        self._engine = engine
        self._menu = Container(1280, 720).set_child_alignment(ChildAlignment.CENTER)

        self._button = (
            Container(200, 100)
            .set_background_color((207, 178, 171))
            .set_border((0, 0, 0))
            .set_child(Text("Settings", FontManager.get("sys", "Arial", 30), (0, 0, 0)))
        )

        self._menu.set_child(self._button)

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        if self._button.contains(pygame.mouse.get_pos()):
            from screens.main_menu_screen import MainMenuScreen
            self._engine.set_screen(MainMenuScreen(self._engine))

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._menu.render(window)
