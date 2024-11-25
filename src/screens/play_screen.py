from math import floor

import pygame
from pygame import Surface

from components import ChildAlignment, ColorPicker, Container, NonogramElement, Text
from core import Nonogram
from engine import Engine
from events import Event, EventType, Key, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class PlayScreen(Screen):
    _engine: Engine
    _nonogram: Nonogram
    _nonogram_element: NonogramElement
    _has_color_picker: bool
    _color_picker: ColorPicker
    _completed_text: Surface

    def __init__(self, engine: Engine, nonogram: Nonogram):
        self._engine = engine
        self._width, self._height = engine.window_size
        self._nonogram = nonogram
        self._has_color_picker = len(nonogram.used_colors) > 1

        self._background = Container(self._width, self._height).set_image("bg.jpg")

        columns = nonogram.size[0] + max([len(row) for row in nonogram.horizontal_hints])
        rows = nonogram.size[1] + max([len(column) for column in nonogram.vertical_hints])

        grid_ratio = columns / rows
        window_ratio = self._width / self._height

        limiting_grid_side = columns if grid_ratio > window_ratio else rows
        limiting_window_side = self._width if grid_ratio > window_ratio else self._height
        block_size = floor(limiting_window_side * 0.9 / limiting_grid_side)

        self._nonogram_element = NonogramElement(nonogram, block_size, 1)
        self._nonogram_container = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER)
            .set_child(self._nonogram_element)
        )

        if self._has_color_picker:
            self._color_picker = ColorPicker(self._nonogram_element, nonogram.used_colors, int(self._height * 0.05), 1)
            self._color_picker_container = (
                Container(self._width, self._height)
                .set_child_alignment(ChildAlignment.CENTER_RIGHT)
                .set_child(
                    Container(
                        self._color_picker.size[0] + int(self._height * 0.05),
                        self._color_picker.size[1] + int(self._height * 0.05)
                    )
                    .set_child(self._color_picker)
                )
            )

        self._return_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1), 25)
            .set_position((20, 20))
            .set_background_color((224, 91, 93))
            .set_child(Text("Return", engine.regular_font, (0, 0, 0)))
        )

        self._completed_text = engine.regular_font.render("completed!", True, (0, 0, 0))

    def on_any_event(self, event: Event) -> None:
        self._nonogram_element.on_any_event(event)
        if self._has_color_picker:
            self._color_picker.on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        if key_event.key == Key.ESCAPE:
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine, self._nonogram.type))

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._return_button.contains(mouse_pos):
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine, self._nonogram.type))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        mouse_pos = pygame.mouse.get_pos()

        cursor_in_clickable = self._return_button.contains(mouse_pos)

        pygame.mouse.set_cursor(self._engine.hand_cursor if cursor_in_clickable else self._engine.arrow_cursor)

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def save(self) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()

        self._background.render(window)
        self._nonogram_container.render(window)

        if self._has_color_picker:
            self._color_picker_container.render(window)

        self._return_button.render(window)

        if self._nonogram.is_completed:
            window.blit(self._completed_text, (20, 50))
