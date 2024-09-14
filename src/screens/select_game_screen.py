import pygame

from components import ChildAlignment, Column, Container, Row, Text, HorizontalAlignment
from core.nonogram import Nonogram
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen

class SelectGameScreen(Screen):
    _engine: Engine

    def __init__(self, engine: Engine):
        self._engine = engine
        self._width, self._height = engine.window_size
        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER)
            .set_border((0, 132, 134))
            .set_background_color((0, 132, 134))
            .set_image("assets/textures/select.jpg")
        )
        row1= Row()
        self._play_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((198, 191, 166))
            .set_border((0, 0, 0, 0))
            .set_child(Text("PLAY", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        self._back_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((198, 191, 166))
            .set_border((0, 0, 0, 0))
            .set_child(Text("BACK", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        row1.add_element(self._back_button)
        row1.add_element(self._play_button)
        row1.set_padding(300)

        container1 = (
            Container(self._width, int(self._height * 0.2))
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
            .set_child(row1)
        )
        container2 = (
            Container(self._width, int(self._height * 0.6))
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
        )
        container3 = (
            Container(self._width, int(self._height * 0.2))
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
        )
        self._column = (
            Column()
            .add_element(container1)
            .add_element(container2)
            .add_element(container3)
        )
        self._base.set_child(self._column)

    def on_all_events(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._play_button.contains(mouse_pos):
            from screens.play_screen import PlayScreen
            nonogram = Nonogram.from_pre_made(16647)
            self._engine.set_screen(PlayScreen(self._engine, nonogram))

        if self._back_button.contains(mouse_pos):
            from screens.main_menu_screen import MainMenuScreen
            self._engine.set_screen(MainMenuScreen(self._engine))


    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)