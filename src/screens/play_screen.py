import pygame
from pygame import Surface

from assets import FontManager
from components import ChildAlignment, ColorPicker, Container, NonogramElement
from core import Nonogram
from engine import Engine
from events import Event, Key, KeyEvent, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class PlayScreen(Screen):
    _engine: Engine
    _menu: Container
    _nonogram: Nonogram
    _nonogram_element: NonogramElement
    _has_color_picker: bool
    _color_picker: ColorPicker
    _completed_text: Surface

    def __init__(self, engine: Engine, nonogram: Nonogram):
        self._engine = engine
        self._menu = Container(*engine.window_size).set_child_alignment(ChildAlignment.CENTER)
        self._nonogram = nonogram
        self._nonogram_element = NonogramElement(nonogram, 25, 1)
        self._has_color_picker = len(nonogram.used_colors) > 1
        if self._has_color_picker:
            self._color_picker = ColorPicker(self._nonogram_element, nonogram.used_colors, 50, 1)
        self._menu.set_child(self._nonogram_element)
        self._completed_text = (FontManager.get("sys", "Arial", 30)
                                .render("completed!", True, (0, 0, 0)))


    def on_any_event(self, event: Event) -> None:
        self._nonogram_element.on_any_event(event)
        if self._has_color_picker:
            self._color_picker.on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        if key_event.key == Key.ESCAPE:
            from screens.main_menu_screen import MainMenuScreen
            self._engine.set_screen(MainMenuScreen(self._engine))

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        pass

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def save(self) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._menu.render(window)
        if self._has_color_picker:
            self._color_picker.render(window)

        if self._nonogram.is_completed:
            window.blit(self._completed_text, (0, 0))
