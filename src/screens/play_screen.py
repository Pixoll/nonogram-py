import pygame
from pygame import Surface

from assets import FontManager
from components import ChildAlignment, ColorPicker, Container, NonogramElement, Row, Text
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
        self._nonogram = nonogram
        self._has_color_picker = len(nonogram.used_colors) > 1

        columns = nonogram.size[0] + max([len(row) for row in nonogram.horizontal_hints])
        rows = nonogram.size[1] + max([len(column) for column in nonogram.vertical_hints])
        window_width, window_height = engine.window_size

        nonogram_container_size = (
            int(window_width * 0.875) if self._has_color_picker else window_width - 20,
            window_height - 20
        )

        grid_ratio = columns / rows
        window_ratio = window_width / window_height

        limiting_grid_side = columns if grid_ratio > window_ratio else rows
        limiting_window_side = window_width if grid_ratio > window_ratio else window_height
        block_size = round(limiting_window_side * 0.875 / limiting_grid_side)

        self._nonogram_element = NonogramElement(nonogram, block_size, 1)
        nonogram_container = (Container(*nonogram_container_size)
                              .set_child_alignment(ChildAlignment.CENTER)
                              .set_child(self._nonogram_element))

        base: Row[Container] = Row().add_element(nonogram_container)

        if self._has_color_picker:
            self._color_picker = ColorPicker(self._nonogram_element, nonogram.used_colors, 50, 1)
            color_picker_size = (engine.window_size[0] - nonogram_container_size[0], nonogram_container_size[1])
            color_picker_container = (Container(*color_picker_size)
                                      .set_child_alignment(ChildAlignment.CENTER)
                                      .set_child(self._color_picker))
            base.add_element(color_picker_container)

        self._back_button = (Container(100, 50)
                             .set_position((20, 20))
                             .set_background_color((224, 91, 93))
                             .set_border((224, 91, 93))
                             .set_child_alignment(ChildAlignment.CENTER)
                             .set_child(Text("Back", FontManager.get("sys", "Arial", 20), (0, 0, 0))))

        self._completed_text = (FontManager.get("sys", "Arial", 30)
                                .render("completed!", True, (0, 0, 0)))

    def on_any_event(self, event: Event) -> None:
        self._nonogram_element.on_any_event(event)
        if self._has_color_picker:
            self._color_picker.on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        if key_event.key == Key.ESCAPE:
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine))

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._back_button.contains(mouse_pos):
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine))

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def save(self) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()

        self._nonogram_element.render(window)
        if self._has_color_picker:
            self._color_picker.render(window)

        self._back_button.render(window)

        if self._nonogram.is_completed:
            window.blit(self._completed_text, (20, 50))
