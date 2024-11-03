import tkinter as tk
from tkinter import filedialog

import pygame

from components import ChildAlignment, Column, Container, DimensionSelector, HorizontalAlignment, RecentColors, Row, \
    Text, VerticalAlignment
from components.colors import Colors
from components.create_nanogram import CreateNanogram
from components.gradient_color import GradientColor
from components.text_field import TextField
from engine import Engine
from events import Event, EventType, KeyEvent, MouseButton, MouseButtonEvent, MouseMotionEvent, QuitEvent
from screens.screen import Screen

root = tk.Tk()
root.withdraw()


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
        self.column2 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.03))
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
            .set_child(self.column2)
        )

        # column 1 elements

        # row 1 elements
        row2 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._width * 0.05))
        column1.add_element(row2)

        self._upload_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Generate", pygame.font.SysFont("Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._upload_button)

        self._randomizer_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Randomized", pygame.font.SysFont("Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._randomizer_button)

        self._eraser_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Erase all", pygame.font.SysFont("Arial", 15), (0, 0, 0)))
        )
        row2.add_element(self._eraser_button)

        #  row 2 elements
        row3 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._height * 0.05))

        self.color_gradient = GradientColor((255, 0, 0), 25, 1)
        self.colors = Colors(3, 0)
        self.lasts_colors = RecentColors(40, 0)

        row3.add_element(self.color_gradient)
        row3.add_element(self.colors)
        row3.add_element(self.lasts_colors)
        column1.add_element(row3)

        self._save_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Save", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._save_button)

        self._exit_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Exit", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        column1.add_element(self._exit_button)

        # column 2 elements
        row4 = Row().set_alignment(VerticalAlignment.CENTER)
        self.dimension_selector1 = DimensionSelector(
            default_value=100,
            font=pygame.font.Font(None, 40),
            inactive_color=(0, 0, 0),
            active_color=(255, 255, 255),
            max_width=int(self._width * 0.035),
        )
        self.x_dimension = (
            Container(int(self._width * 0.1), int(self._height * 0.05))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(self.dimension_selector1)
        )
        row4.add_element(self.x_dimension)
        self.dimension_selector2 = DimensionSelector(
            default_value=100,
            font=pygame.font.Font(None, 40),
            inactive_color=(0, 0, 0),
            active_color=(255, 255, 255),
            max_width=int(self._width * 0.035),
        )
        self.y_dimension = (
            Container(int(self._width * 0.1), int(self._height * 0.05))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(self.dimension_selector2)
        )
        row4.add_element(self.y_dimension)
        row4.add_element(Container(20, 0))
        self._resize_button = (
            Container(int(self._width * 0.1), int(self._height * 0.05))
            .set_background_color((224, 99, 159))
            .set_border((0, 0, 0, 0))
            .set_child(Text("Resize", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        )
        row4.add_element(self._resize_button)
        self.column2.add_element(row4)

        self.board = CreateNanogram(100, 100, 1, int(self._width * 0.4)).set_selected_color((255, 0, 0))
        self.board_base = (Container(int(self._width * 0.4), int(self._width * 0.4)).set_child(self.board)
                           .set_child_alignment(ChildAlignment.CENTER).set_border((0, 0, 0, 0))
                           )
        self.column2.add_element(self.board_base)

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
        self.column2.add_element(self.nanogram_name)

        row1.add_element(container1).add_element(container2)
        self._base.set_child(row1)

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        self.text_field.on_any_event(event=key_event)
        self.nanogram_name._update_child_position()

        self.dimension_selector1.on_any_event(event=key_event)
        self.x_dimension._update_child_position()

        self.dimension_selector2.on_any_event(event=key_event)
        self.y_dimension._update_child_position()

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        if self._resize_button.contains(mouse_pos):
            if (self.dimension_selector1.get_value() != self.dimension_selector1.get_default_value()) or (
                    self.dimension_selector2.get_value() != self.dimension_selector2.get_default_value()):
                self.board = CreateNanogram(self.dimension_selector1.get_value(), self.dimension_selector2.get_value(),
                                            1, int(self._width * 0.4)).set_selected_color(
                    (255, 0, 0)).set_selected_color(self.color_gradient.get_color())
                self.dimension_selector1.set_default_value(self.dimension_selector1.get_value())
                self.dimension_selector2.set_default_value(self.dimension_selector2.get_value())
                self.board_base.set_child(self.board)

        if self.dimension_selector1.on_any_event(event):
            self.dimension_selector1.on_any_event(event)
            self.x_dimension.set_child(self.dimension_selector1)

        if self.dimension_selector2.on_any_event(event):
            self.dimension_selector2.on_any_event(event)
            self.y_dimension.set_child(self.dimension_selector2)

        if self._exit_button.contains(mouse_pos):
            from screens.workshop_screen import WorkshopScreen
            self._engine.set_screen(WorkshopScreen(self._engine))

        if self._save_button.contains(mouse_pos):
            self.board.set_name(self.text_field.get_text())
            self.board.save()

        if self._eraser_button.contains(mouse_pos):
            self.board.clear()

        if self._randomizer_button.contains(mouse_pos):
            self.board.randomizer()

        if self._upload_button.contains(mouse_pos):
            file_path = filedialog.askopenfilename(
                title="Selecciona una imagen",
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
            )
            if file_path:
                self.board.generate_from_image(file_path)

        self.board.on_any_event(event)
        self.color_gradient.on_any_event(event)

        if self.text_field.on_any_event(event):
            self.text_field.on_any_event(event)
            self.nanogram_name.set_child(self.text_field)

        if self.color_gradient.contains(mouse_pos):
            new_color = self.color_gradient.get_color()
            self.board.set_selected_color(new_color)
            self.lasts_colors.add_color(new_color)

        if self.colors.contains(mouse_pos):
            self.colors.on_any_event(event)
            self.color_gradient.paint_gradient(self.colors.get_selected_color())
            self.board.set_selected_color(self.color_gradient.get_color())

        if self.lasts_colors.contains(mouse_pos):
            self.lasts_colors.on_any_event(event)
            self.board.set_selected_color(self.lasts_colors.get_current_color())

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._base.render(window)
