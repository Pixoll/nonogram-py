import pygame
from pygame import font, Surface

from components import ChildAlignment, ColorPicker, Container, NonogramElement
from core.nonogram import Nonogram
from engine import Engine
from events import Event, Key, KeyEvent, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class PlayScreen(Screen):
    _engine: Engine
    _menu: Container
    _nonogram: Nonogram
    _nonogram_element: NonogramElement
    _color_picker: ColorPicker
    _completed_text: Surface

    def __init__(self, engine: Engine, nonogram: Nonogram):
        self._engine = engine
        self._menu = Container(1280, 720).set_child_alignment(ChildAlignment.CENTER)
        self._nonogram = nonogram
        self._nonogram_element = NonogramElement(nonogram, 25, 1)
        self._color_picker = ColorPicker(self._nonogram_element, nonogram.used_colors, 50, 1)
        self._menu.set_child(self._nonogram_element)
        self._completed_text = font.SysFont("Arial", 30).render("completed!", True, (0, 0, 0))

    def on_all_events(self, event: Event) -> None:
        self._nonogram_element.on_all_events(event)
        self._color_picker.on_all_events(event)

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

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._menu.render(window)
        self._color_picker.render(window)

        if self._nonogram.is_completed:
            window.blit(self._completed_text, (0, 0))
