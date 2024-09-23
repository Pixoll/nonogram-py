import pygame

from components import ChildAlignment, Column, Container, Row, Text, HorizontalAlignment, VerticalAlignment
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
            .set_border((0, 0, 0, 0))
            .set_background_color((0, 0, 0, 0))
        )

        column1 = Column().set_alignment(HorizontalAlignment.LEFT).set_padding(int(self._height * 0.05))
        row1 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._width * 0.18))

        self._my_button = (
            Container(int(self._width * 0.2), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("My nanograms", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._my_button)

        self._create_button = (
            Container(int(self._width * 0.2), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Create", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._create_button)

        self._saved_button = (
            Container(int(self._width * 0.2), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Saved", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._saved_button)

        column1.add_element(Container(0, int(self._height * 0.08)))

        self._return_button = (
            Container(int(self._width * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Return", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._return_button)

        row1.add_element(column1)

        column2 = Column()

        self._imagen_referencial = (
            Container(int(self._width * 0.4), int(self._width * 0.3))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("imagen1", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column2.add_element(self._imagen_referencial)

        self._informacion_referencial = (
            Container(int(self._width * 0.4), int(self._width * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("informacion1", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )

        column2.add_element(self._informacion_referencial)
        row1.add_element(column2)

        self._base.set_child(row1)
    def on_all_events(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._return_button.contains(mouse_pos):
            from screens.main_menu_screen import MainMenuScreen
            self._engine.set_screen(MainMenuScreen(self._engine))

        if self._create_button.contains(mouse_pos):
            from screens.create_screen import CreateScreen
            self._engine.set_screen(CreateScreen(self._engine))

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        if event.type != EventType.MOUSE_MOTION:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._my_button.contains(mouse_pos):
            self._informacion_referencial.set_child(Text("informacion1", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
            self._imagen_referencial.set_child(Text("imagen1", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        elif self._create_button.contains(mouse_pos):
            self._informacion_referencial.set_child(Text("informacion2", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
            self._imagen_referencial.set_child(Text("imagen2", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        elif self._saved_button.contains(mouse_pos):
            self._informacion_referencial.set_child(Text("informacion3", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
            self._imagen_referencial.set_child(Text("imagen3", pygame.font.SysFont("Arial", 30), (0, 0, 0)))


    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
