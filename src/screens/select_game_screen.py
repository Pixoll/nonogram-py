import pygame

from components import ChildAlignment, Column, Container, Row, RowOfNonograms, Text
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class SelectGameScreen(Screen):
    _engine: Engine
    _row_of_pre_made_nonograms: RowOfNonograms

    def __init__(self, engine: Engine):
        self._engine = engine
        self._width, self._height = engine.window_size
        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER)
            .set_border((0, 132, 134))
            .set_background_color((0, 132, 134))
            .set_image("select.jpg")
        )
        row1 = Row()
        self._play_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((198, 191, 166))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Play", engine.regular_font, (0, 0, 0)))
        )
        self._back_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((198, 191, 166))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Back", engine.regular_font, (0, 0, 0)))
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

        self._row_of_pre_made_nonograms = RowOfNonograms(self._width, int(self._height * 0.3), "pre_made")
        self._row_of_user_made_nonograms = RowOfNonograms(self._width, int(self._height * 0.3), "user_made")

        container2 = (
            Container(self._width, self._row_of_pre_made_nonograms.size[1])
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
            .set_child(self._row_of_pre_made_nonograms)
        )
        container3 = (
            Container(self._width, int(self._height * 0.1))
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
        )
        container4 = (
            Container(self._width, self._row_of_user_made_nonograms.size[1])
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
            .set_child(self._row_of_user_made_nonograms)
        )
        container5 = (
            Container(
                self._width,
                self._height - container1.size[1] - container2.size[1] - container3.size[1] - container4.size[1]
            )
            .set_background_color((0, 0, 0, 200))
            .set_border((0, 0, 0, 0))
        )

        self._column = (
            Column()
            .add_element(container1)
            .add_element(container2)
            .add_element(container3)
            .add_element(container4)
            .add_element(container5)
        )

        self._base.set_child(self._column)

    def on_any_event(self, event: Event) -> None:
        self._row_of_pre_made_nonograms.on_any_event(event)
        self._row_of_user_made_nonograms.on_any_event(event)

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._row_of_pre_made_nonograms.contains(mouse_pos):
            self._row_of_user_made_nonograms.deselect()

        if self._row_of_user_made_nonograms.contains(mouse_pos):
            self._row_of_pre_made_nonograms.deselect()

        if self._play_button.contains(mouse_pos):
            from screens.play_screen import PlayScreen
            selected_nonogram = self._row_of_pre_made_nonograms.get_selected_nonogram()
            if selected_nonogram:
                self._engine.set_screen(PlayScreen(self._engine, selected_nonogram))
            selected_nonogram = self._row_of_user_made_nonograms.get_selected_nonogram()
            if selected_nonogram:
                self._engine.set_screen(PlayScreen(self._engine, selected_nonogram))

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
