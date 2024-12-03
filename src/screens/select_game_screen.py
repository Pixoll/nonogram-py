import pygame

from components import Container, Row, NonogramsRow, Text, VerticalAlignment
from core import nonogram_type_t, NonogramSize
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class SelectGameScreen(Screen):
    _engine: Engine

    def __init__(self, engine: Engine, nonogram_type: nonogram_type_t):
        self._engine = engine
        self._width, self._height = engine.window_size
        self._nonogram_type = nonogram_type
        self._selected_size = NonogramSize.SMALL

        self._background = Container(self._width, self._height).set_image("bg.jpg")

        self._play_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1), 25)
            .set_position((int(self._width * 0.45), int(self._height * 0.85)))
            .set_background_color((108, 224, 124))
            .set_child(Text("Play", engine.regular_font, (0, 0, 0)))
        )

        self._return_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1), 25)
            .set_position((20, 20))
            .set_background_color((224, 91, 93))
            .set_child(Text("Return", engine.regular_font, (0, 0, 0)))
        )

        row_pos = (0, int(self._height * 0.1))
        self._nonograms_rows = {
            size: NonogramsRow(
                self._width,
                int(self._height * 0.8),
                nonogram_type,
                size,
                engine.regular_font,
                engine.small_font
            ).set_position(row_pos) for size in NonogramSize
        }

        header_height = int(self._height * 0.1)
        header_padding = int(self._width * 0.02)
        arrow_size = int(header_height * 0.6)

        self._left_arrow = (
            Container(arrow_size, arrow_size)
            .set_image("left_arrow.png", False)
            .fit_to_image()
            .set_hidden(True)
        )
        self._right_arrow = (
            Container(arrow_size, arrow_size)
            .set_image("right_arrow.png", False)
            .fit_to_image()
        )

        self._size_header: dict[NonogramSize, Container] = {
            size: (
                Container(self._width, header_height)
                .set_position((0, 20))
                .set_child(
                    Row()
                    .set_alignment(VerticalAlignment.CENTER)
                    .set_padding(header_padding)
                    .add_element(self._left_arrow)
                    .add_element(
                        Container(int(self._width * 0.2), int(self._height * 0.1), 25)
                        .set_background_color((255, 255, 128))
                        .set_child(Text(size.name.capitalize(), engine.regular_font, (0, 0, 0)))
                    )
                    .add_element(self._right_arrow)
                )
            ) for size in NonogramSize
        }

    def on_any_event(self, event: Event) -> None:
        self._nonograms_rows[self._selected_size].on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if not self._left_arrow.hidden and self._left_arrow.contains(mouse_pos):
            self._right_arrow.set_hidden(False)
            self._selected_size = NonogramSize(int(self._selected_size) - 1)
            if self._selected_size == NonogramSize.SMALL:
                self._left_arrow.set_hidden(True)
                pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if not self._right_arrow.hidden and self._right_arrow.contains(mouse_pos):
            self._left_arrow.set_hidden(False)
            self._selected_size = NonogramSize(int(self._selected_size) + 1)
            if self._selected_size == NonogramSize.HUGE:
                self._right_arrow.set_hidden(True)
                pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if self._play_button.contains(mouse_pos):
            from screens.play_screen import PlayScreen
            selected_nonogram = self._nonograms_rows[self._selected_size].get_selected_nonogram()
            if selected_nonogram is not None:
                self._engine.set_screen(PlayScreen(self._engine, selected_nonogram))
                pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if self._return_button.contains(mouse_pos):
            if self._nonogram_type == "pre_made":
                from screens.main_menu_screen import MainMenuScreen
                self._engine.set_screen(MainMenuScreen(self._engine))
            else:
                from screens.workshop_screen import WorkshopScreen
                self._engine.set_screen(WorkshopScreen(self._engine))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        mouse_pos = pygame.mouse.get_pos()

        cursor_in_clickable = (self._play_button.contains(mouse_pos)
                               or self._return_button.contains(mouse_pos)
                               or (self._selected_size != NonogramSize.SMALL and self._left_arrow.contains(mouse_pos))
                               or (self._selected_size != NonogramSize.HUGE and self._right_arrow.contains(mouse_pos)))

        pygame.mouse.set_cursor(self._engine.hand_cursor if cursor_in_clickable else self._engine.arrow_cursor)

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()

        self._background.render(window)
        self._size_header[self._selected_size].render(window)
        self._nonograms_rows[self._selected_size].render(window)
        self._return_button.render(window)
        self._play_button.render(window)
