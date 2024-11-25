import pygame

from components import ChildAlignment, Column, Container, Row, RowOfNonograms, Text
from core import nonogram_type_t
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class SelectGameScreen(Screen):
    _engine: Engine
    _row_of_nonograms: RowOfNonograms

    def __init__(self, engine: Engine, nonogram_type: nonogram_type_t):
        self._engine = engine
        self._width, self._height = engine.window_size
        self._nonogram_type = nonogram_type

        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.TOP_CENTER)
            .set_image("bg.jpg")
        )

        row1 = Row()
        self._play_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1), 25)
            .set_background_color((108, 224, 124))
            .set_child(Text("Play", engine.regular_font, (0, 0, 0)))
        )
        self._return_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1), 25)
            .set_background_color((224, 91, 93))
            .set_child(Text("Return", engine.regular_font, (0, 0, 0)))
        )
        row1.add_element(self._return_button)
        row1.add_element(self._play_button)
        row1.set_padding(300)

        container1 = Container(self._width, int(self._height * 0.2)).set_child(row1)

        self._row_of_nonograms = RowOfNonograms(self._width, int(self._height * 0.3), nonogram_type)

        container2 = (
            Container(self._width, self._row_of_nonograms.size[1])
            .set_background_color((0, 0, 0, 128))
            .set_child(self._row_of_nonograms)
        )

        column = (
            Column()
            .add_element(container1)
            .add_element(Container(self._width, int(self._height * 0.1)))
            .add_element(container2)
        )

        self._base.set_child(column)

    def on_any_event(self, event: Event) -> None:
        self._row_of_nonograms.on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._play_button.contains(mouse_pos):
            from screens.play_screen import PlayScreen
            selected_nonogram = self._row_of_nonograms.get_selected_nonogram()
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
                               or self._return_button.contains(mouse_pos))

        pygame.mouse.set_cursor(self._engine.hand_cursor if cursor_in_clickable else self._engine.arrow_cursor)

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
