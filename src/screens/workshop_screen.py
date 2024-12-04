import pygame

from assets import FontManager
from components import ChildAlignment, Column, Container, HorizontalAlignment, Text
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class WorkshopScreen(Screen):
    _engine: Engine

    def __init__(self, engine: Engine):
        self._engine = engine
        self._width, self._height = engine.window_size

        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER)
            .set_image("bg.jpg")
            .set_child(
                Container(self._width, self._height)
                .set_child_alignment(ChildAlignment.CENTER)
                .set_image("menu_background.png")
            )
        )

        self._title: Container = (
            Container(self._width, self._height)
            .set_child(
                Container(self._width, int(self._height * 0.95))
                .set_child_alignment(ChildAlignment.TOP_CENTER)
                .set_child(
                    Text("Workshop", FontManager.get_default(int(self._width * 0.04)), (0, 0, 0))
                )
            )
        )

        column1 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.04))
        # row1 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._width * 0.18))

        self._my_nonograms_button = (
            Container(int(self._width * 0.2), int(self._height * 0.1), 25)
            .set_background_color((54, 169, 251))
            .set_border((0, 0, 0, 0))
            .set_child(Text("My nonograms", engine.regular_font, (0, 0, 0)))
        )
        column1.add_element(self._my_nonograms_button)

        self._create_button = (
            Container(int(self._width * 0.2), int(self._height * 0.1), 25)
            .set_background_color((54, 169, 251))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Create", engine.regular_font, (0, 0, 0)))
        )
        column1.add_element(self._create_button)

        # self._saved_button = (
        #     Container(int(self._width * 0.2), int(self._height * 0.1), 25)
        #     .set_background_color((54, 169, 251))
        #     .set_border((0, 0, 0, 0))
        #     .set_child(Text("Saved", engine.regular_font, (0, 0, 0)))
        # )
        # column1.add_element(self._saved_button)

        # column1.add_element(Container(0, int(self._height * 0.08), 25))

        self._return_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1), 25)
            .set_background_color((224, 91, 93))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Return", engine.regular_font, (0, 0, 0)))
        )
        column1.add_element(self._return_button)

        # row1.add_element(column1)

        # column2 = Column()
        #
        # self._ref_image = (
        #     Container(int(self._width * 0.4), int(self._width * 0.3))
        #     .set_background_color((224, 130, 178))
        #     .set_border((0, 0, 0, 0))
        #     .set_child(Text("image1", engine.regular_font, (0, 0, 0)))
        # )
        # column2.add_element(self._ref_image)
        #
        # self._ref_info = (
        #     Container(int(self._width * 0.4), int(self._width * 0.1))
        #     .set_background_color((224, 130, 178))
        #     .set_border((0, 0, 0, 0))
        #     .set_child(Text("info1", engine.regular_font, (0, 0, 0)))
        # )
        #
        # column2.add_element(self._ref_info)
        # row1.add_element(column2)

        self._base.child.set_child(column1)

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._my_nonograms_button.contains(mouse_pos):
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine, "user_made"))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if self._create_button.contains(mouse_pos):
            from screens.create_screen import CreateScreen
            self._engine.set_screen(CreateScreen(self._engine, (25, 25)))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if self._return_button.contains(mouse_pos):
            from screens.main_menu_screen import MainMenuScreen
            self._engine.set_screen(MainMenuScreen(self._engine))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        mouse_pos = pygame.mouse.get_pos()

        cursor_in_clickable = (self._my_nonograms_button.contains(mouse_pos)
                               or self._create_button.contains(mouse_pos)
                               # or self._saved_button.contains(mouse_pos)
                               or self._return_button.contains(mouse_pos))

        pygame.mouse.set_cursor(self._engine.hand_cursor if cursor_in_clickable else self._engine.arrow_cursor)

        # if self._my_nonograms_button.contains(mouse_pos):
        #     self._ref_info.set_child(Text("info1", self._engine.regular_font, (0, 0, 0)))
        #     self._ref_image.set_child(Text("image1", self._engine.regular_font, (0, 0, 0)))
        #     return
        #
        # if self._create_button.contains(mouse_pos):
        #     self._ref_info.set_child(Text("info2", self._engine.regular_font, (0, 0, 0)))
        #     self._ref_image.set_child(Text("image2", self._engine.regular_font, (0, 0, 0)))
        #     return
        #
        # if self._saved_button.contains(mouse_pos):
        #     self._ref_info.set_child(Text("info3", self._engine.regular_font, (0, 0, 0)))
        #     self._ref_image.set_child(Text("image3", self._engine.regular_font, (0, 0, 0)))
        #     return

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
        self._title.render(window)
