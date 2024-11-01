import pygame

from assets import FontManager
from components import ChildAlignment, Column, Container, HorizontalAlignment, Row, Text, VerticalAlignment
from components.colors import Colors
from components.create_nanogram import CreateNanogram
from components.gradient_color import GradientColor
from components.text_field import TextField
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen


class CreateScreen(Screen):
    _engine: Engine
    _menu: Container
    _button: Container

    def __init__(self, engine: Engine):
        self._engine = engine
        self._width, self._height = engine.window_size

        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER_LEFT)
            .set_border((0, 0, 0, 0))
            .set_background_color((0, 0, 0, 0))
        )

        column1 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.05))
        column2 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.05))
        row1 = Row().set_alignment(VerticalAlignment.CENTER)
        container1 = (
            Container(int(self._width * 0.4), int(self._height))
            .set_background_color((0, 0, 0, 50))
            .set_border((0, 0, 0, 50))
            .set_child(column1)
        )
        container2 = (
            Container(int(self._width * 0.6), int(self._height))
            .set_background_color((0, 0, 0, 150))
            .set_border((0, 0, 0, 150))
            .set_child(column2)
        )

        # column 1 elements

        # row 1 elements
        row2 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._width * 0.05))
        column1.add_element(row2)

        self._upload_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Generate", FontManager.get("sys", "Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._upload_button)

        self._pencil_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Randomized", FontManager.get("sys", "Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._pencil_button)

        self._eraser_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Erase all", FontManager.get("sys", "Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._eraser_button)

        #  row 2 elements
        row3 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._height * 0.05))
        self.color_gradient = GradientColor((255, 0, 0), 25, 1)
        row3.add_element(self.color_gradient)
        self.colors = Colors(3, 0)

        row3.add_element(self.colors)

        column1.add_element(row3)

        self._save_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Save", FontManager.get("sys", "Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._save_button)

        self._exit_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Exit", FontManager.get("sys", "Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._exit_button)

        # column 2 elements
        self.board = CreateNanogram(20, 20, 1)
        board_base = (Container(max(self.board.size), max(self.board.size)).set_child(self.board)
                      .set_child_alignment(ChildAlignment.CENTER).set_border((0, 0, 0, 0)))
        self.board.set_selected_color((255, 0, 0))
        column2.add_element(board_base)

        self.text_field = TextField(
            text="Level name...",
            font=pygame.font.Font(None, 40),
            inactive_color=(0, 0, 0),
            active_color=(255, 255, 255),
            max_width=int(self._width * 0.3),
        )
        self.nanogram_name = (
            Container(int(self._width * 0.3), int(self._height * 0.08))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(self.text_field)
        )
        column2.add_element(self.nanogram_name)

        row1.add_element(container1).add_element(container2)
        self._base.set_child(row1)

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        self.text_field.on_any_event(event=key_event)
        self.nanogram_name._update_child_position()

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._exit_button.contains(mouse_pos):
            from screens.workshop_screen import WorkshopScreen
            self._engine.set_screen(WorkshopScreen(self._engine))

        if self._save_button.contains(mouse_pos):
            self.board.set_name(self.text_field.get_text())
            self.board.save()

        if self._eraser_button.contains(mouse_pos):
            self.board.clear()

        self.board.on_any_event(event)
        self.color_gradient.on_any_event(event)
        if self.text_field.on_any_event(event):
            self.text_field.on_any_event(event)
            self.nanogram_name.set_child(self.text_field)

        if self.color_gradient.contains(mouse_pos):
            new_color = self.color_gradient.get_color()
            self.board.set_selected_color(new_color)

        if self.colors.contains(mouse_pos):
            new_gradient = self.colors.on_any_event(event)
            self.color_gradient.paint_gradient(new_gradient)
            new_color = self.color_gradient.get_color()
            self.board.set_selected_color(new_color)

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
