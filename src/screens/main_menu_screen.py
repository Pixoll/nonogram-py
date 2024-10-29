import pygame

from components import ChildAlignment, Column, Container, HorizontalAlignment, Row, Text
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class MainMenuScreen(Screen):
    _engine: Engine

    def __init__(self, engine: Engine):
        self._engine = engine
        self._width, self._height = engine.window_size

        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER)
            .set_border((0, 132, 134))
            .set_background_color((0, 132, 134))
            .set_image("assets/textures/bg_main_menu.jpg")
        )

        column1 = Column()
        column2 = Column()

        title = (
            Container(int(self._width * 0.4), int(self._height * 0.3))
            .set_background_color((255, 255, 255))
            .set_border((255, 255, 255))
            .set_child(
                Text(
                    "NANOGRAM",
                    pygame.font.SysFont("Arial", 80),
                    (99, 99, 224)
                )
                .set_color((152, 99, 224))
            )
        )

        column1.add_element(title)

        self._play_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((207, 178, 171))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Play", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )

        self._workshop_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((207, 224, 99))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Workshop", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )

        self._settings_button = (
            Container(int(self._width * 0.3), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Statistics", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )

        self._exit_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Exit", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )

        (column2.add_element(self._play_button)
         .add_element(self._workshop_button)
         .add_element(self._settings_button)
         .add_element(self._exit_button)
         .set_padding(int(self._height * 0.08))
         .set_alignment(HorizontalAlignment.LEFT))

        container1 = (
            Container(int(self._width * 0.6), self._height)
            .set_background_color((255, 255, 255, 0))
            .set_border((0, 0, 0, 0))
            .set_child(column1)
        )

        container2 = (
            Container(int(self._width * 0.4), self._height)
            .set_background_color((0, 0, 0, 150))
            .set_border((0, 0, 0, 0))
            .set_child(column2)
        )

        self._row1 = (
            Row()
            .add_element(container1)
            .add_element(container2)
        )

        self._base.set_child(self._row1)

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._play_button.contains(mouse_pos):
            from screens.select_game_screen import SelectGameScreen
            self._engine.set_screen(SelectGameScreen(self._engine))

        elif self._workshop_button.contains(mouse_pos):
            from screens.workshop_screen import WorkshopScreen
            self._engine.set_screen(WorkshopScreen(self._engine))

        elif self._settings_button.contains(mouse_pos):
            from screens.settings_screen import SettingsScreen
            self._engine.set_screen(SettingsScreen(self._engine))

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
