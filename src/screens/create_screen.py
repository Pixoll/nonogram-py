import time
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
    _base: Container
    _button: Container

    def __init__(self, engine: Engine, default_grid_size: tuple[int, int]):
        self._engine = engine
        self._width, self._height = engine.window_size

        self._base = (
            Container(self._width, self._height)
            .set_child_alignment(ChildAlignment.CENTER_LEFT)
            .set_image("bg.jpg")
        )

        column1 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.05))
        self._column2 = Column().set_alignment(HorizontalAlignment.CENTER).set_padding(int(self._height * 0.03))
        row1 = Row().set_alignment(VerticalAlignment.CENTER)
        container1 = (
            Container(int(self._width * 0.4), int(self._height))
            .set_child(column1)
        )
        container2 = (
            Container(int(self._width * 0.6), int(self._height))
            .set_background_color((0, 0, 0, 128))
            .set_border((0, 0, 0, 128))
            .set_child(self._column2)
        )

        tooltip_size = (int(self._width * 0.1), int(self._height * 0.05))

        row2 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._width * 0.05))
        column1.add_element(row2)

        self._upload_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_image("open_icon.png", False)
            .fit_to_image()
        )
        row2.add_element(self._upload_button)

        self._upload_tooltip: Container = (
            Container(*tooltip_size, 15)
            .set_background_color((255, 255, 255, 128))
            .set_child(Text("Generate from image", engine.small_font, (0, 0, 0)))
        )
        self._show_upload_tooltip = False

        self._randomizer_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_image("randomize_icon.png", False)
            .fit_to_image()
        )
        row2.add_element(self._randomizer_button)

        self._randomizer_tooltip: Container = (
            Container(*tooltip_size, 15)
            .set_background_color((255, 255, 255, 128))
            .set_child(Text("Randomize board", engine.small_font, (0, 0, 0)))
        )
        self._show_randomizer_tooltip = False

        self._erase_all_button = (
            Container(int(self._height * 0.1), int(self._height * 0.1))
            .set_image("erase_all_icon.png", False)
            .fit_to_image()
        )
        row2.add_element(self._erase_all_button)

        self._erase_all_tooltip: Container = (
            Container(*tooltip_size, 15)
            .set_background_color((255, 255, 255, 128))
            .set_child(Text("Clear board", engine.small_font, (0, 0, 0)))
        )
        self._show_erase_all_tooltip = False

        row3 = Row().set_alignment(VerticalAlignment.CENTER).set_padding(int(self._height * 0.05))

        block_size = int(self._height * 0.04)
        self._colors = Colors(block_size // 5, 1)
        self._color_gradient = GradientColor((255, 0, 0), block_size, 1)
        self._lasts_colors = RecentColors(block_size, 1)

        row3.add_element(self._color_gradient)
        row3.add_element(self._colors)
        row3.add_element(self._lasts_colors)
        column1.add_element(row3)

        self._save_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1), 25)
            .set_background_color((108, 224, 124))
            .set_child(Text("Save", engine.regular_font, (0, 0, 0)))
        )
        column1.add_element(self._save_button)

        self._return_button = (
            Container(int(self._width * 0.15), int(self._height * 0.1), 25)
            .set_background_color((224, 91, 93))
            .set_child(Text("Return", engine.regular_font, (0, 0, 0)))
        )
        column1.add_element(self._return_button)

        row4 = Row().set_alignment(VerticalAlignment.CENTER)
        self._dimension_selector1 = DimensionSelector(
            default_grid_size[0],
            engine.regular_font,
            (0, 0, 0),
            (255, 255, 255),
            int(self._width * 0.035),
        )
        self._x_dimension = (
            Container(int(self._width * 0.06), int(self._height * 0.075), 25)
            .set_background_color((54, 169, 251))
            .set_child(self._dimension_selector1)
        )
        row4.add_element(self._x_dimension)

        row4.add_element(Container(13, 0))

        row4.add_element(Text("x", engine.big_font, (0, 0, 0)))

        row4.add_element(Container(10, 0))

        self._dimension_selector2 = DimensionSelector(
            default_grid_size[1],
            engine.regular_font,
            (0, 0, 0),
            (255, 255, 255),
            int(self._width * 0.035),
        )
        self._y_dimension = (
            Container(int(self._width * 0.06), int(self._height * 0.075), 25)
            .set_background_color((54, 169, 251))
            .set_border((0, 0, 0, 0))
            .set_child(self._dimension_selector2)
        )
        row4.add_element(self._y_dimension)

        row4.add_element(Container(20, 0))

        self._resize_button = (
            Container(int(self._width * 0.1), int(self._height * 0.075), 25)
            .set_background_color((54, 169, 251))
            .set_child(Text("Resize", engine.regular_font, (0, 0, 0)))
        )
        row4.add_element(self._resize_button)
        self._column2.add_element(row4)

        self._board = CreateNanogram(*default_grid_size, 1, int(self._width * 0.4)).set_selected_color((255, 0, 0))
        self._board_base = (Container(int(self._width * 0.4), int(self._width * 0.4))
                            .set_child_alignment(ChildAlignment.CENTER)
                            .set_child(self._board))
        self._column2.add_element(self._board_base)

        self._name_field = TextField(
            "Level name...",
            engine.regular_font,
            (0, 0, 0),
            (255, 255, 255),
            int(self._width * 0.3),
        )
        self._nanogram_name = (
            Container(int(self._width * 0.3), int(self._height * 0.075), 25)
            .set_background_color((54, 169, 251))
            .set_child(self._name_field)
        )
        self._column2.add_element(self._nanogram_name)

        row1.add_element(container1).add_element(container2)
        self._base.set_child(row1)

        # ----------------------<| reaction widget |>----------------------

        self._waiting_exit_confirmation = False
        self._exit_time = None

        self._exit_message_popup = Container(
            self._width, self._height
        ).set_background_color((0, 0, 0, 128)).set_child(
            Text(
                "Saved new nonogram",
                engine.regular_font,
                (255, 255, 255)
            )
        )

        self._showing_error_message = False
        self._error_start_time = None
        error_height = int(self._height * 0.1)
        error_y = (self._height - error_height) // 2

        self._error_message_popup = Container(
            self._width, int(self._height * 0.1)
        ).set_background_color((255, 0, 0, 180)).set_child(
            Text(
                "Error occurred!",
                engine.regular_font,
                (255, 255, 255)
            )
        ).set_position((0, error_y))

    def show_error_message(self, message: str) -> None:
        self._error_message_popup.set_child(Text(message, self._engine.regular_font, (255, 255, 255)))
        self._showing_error_message = True
        self._error_start_time = time.time()

    def on_any_event(self, event: Event) -> None:
        pass

    def on_key_event(self, key_event: KeyEvent) -> None:
        if self._waiting_exit_confirmation:
            return

        if self._showing_error_message:
            return

        self._name_field.on_any_event(key_event)
        self._dimension_selector1.on_any_event(key_event)
        self._dimension_selector2.on_any_event(key_event)

    def on_mouse_button_event(self, event: MouseButtonEvent) -> None:
        if self._waiting_exit_confirmation:
            return

        if self._showing_error_message:
            return

        self._board.on_any_event(event)

        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        mouse_pos = pygame.mouse.get_pos()

        self._dimension_selector1.set_active(self._x_dimension.contains(mouse_pos))
        self._dimension_selector2.set_active(self._y_dimension.contains(mouse_pos))
        self._name_field.set_active(self._nanogram_name.contains(mouse_pos))

        self._dimension_selector1.on_any_event(event)
        self._dimension_selector2.on_any_event(event)
        self._color_gradient.on_any_event(event)
        self._name_field.on_any_event(event)

        if self._resize_button.contains(mouse_pos):
            if (self._dimension_selector1.get_value() != self._dimension_selector1.get_default_value()) or (
                    self._dimension_selector2.get_value() != self._dimension_selector2.get_default_value()):
                self._board = (
                    CreateNanogram(
                        self._dimension_selector1.get_value(),
                        self._dimension_selector2.get_value(),
                        1,
                        int(self._width * 0.4)
                    )
                    .set_selected_color((255, 0, 0))
                    .set_selected_color(self._color_gradient.get_color())
                )
                self._dimension_selector1.set_default_value(self._dimension_selector1.get_value())
                self._dimension_selector2.set_default_value(self._dimension_selector2.get_value())
                self._board_base.set_child(self._board)
            return

        if self._return_button.contains(mouse_pos):
            from screens.workshop_screen import WorkshopScreen
            self._engine.set_screen(WorkshopScreen(self._engine))
            pygame.mouse.set_cursor(self._engine.arrow_cursor)
            return

        if self._save_button.contains(mouse_pos):
            self._board.set_name(self._name_field.get_text())

            if self._board.is_empty():
                self.show_error_message("ERROR: Board is empty")
                return
            if self._board.is_nameless():
                self.show_error_message("ERROR: Board is nameless")
                return
            if self._board.has_more_than_128_colors():
                self.show_error_message("ERROR: Board has more than 128 colors")
                return
            if self._board.has_empty_row_or_column_in_between():
                self.show_error_message("ERROR: Board has empty rows or columns in between colored pixels")
                return

            self._board.save()
            self._waiting_exit_confirmation = True
            self._exit_time = time.time()
            return

        if self._erase_all_button.contains(mouse_pos):
            self._board.clear()
            return

        if self._randomizer_button.contains(mouse_pos):
            if self._board.is_empty():
                self.show_error_message("ERROR: Board is empty")
            else:
                self._board.randomizer()
            return

        if self._upload_button.contains(mouse_pos):
            file_path = filedialog.askopenfilename(
                title="Select an image",
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
            )
            if file_path:
                self._board.generate_from_image(file_path)
            return

        if self._color_gradient.contains(mouse_pos):
            new_color = self._color_gradient.get_color()
            self._board.set_selected_color(new_color)
            self._lasts_colors.add_color(new_color)
            self._lasts_colors.reset_color()
            return

        if self._colors.contains(mouse_pos):
            self._colors.on_any_event(event)
            self._color_gradient.paint_gradient(self._colors.get_selected_color())
            self._board.set_selected_color(self._color_gradient.get_color())
            return

        if self._lasts_colors.contains(mouse_pos):
            self._lasts_colors.on_any_event(event)
            self._board.set_selected_color(self._lasts_colors.get_current_color())
            return

    def on_mouse_motion_event(self, event: MouseMotionEvent) -> None:
        mouse_pos = pygame.mouse.get_pos()

        cursor_in_clickable = (self._upload_button.contains(mouse_pos)
                               or self._randomizer_button.contains(mouse_pos)
                               or self._erase_all_button.contains(mouse_pos)
                               or self._save_button.contains(mouse_pos)
                               or self._return_button.contains(mouse_pos)
                               or self._x_dimension.contains(mouse_pos)
                               or self._y_dimension.contains(mouse_pos)
                               or self._resize_button.contains(mouse_pos)
                               or self._nanogram_name.contains(mouse_pos))

        pygame.mouse.set_cursor(self._engine.hand_cursor if cursor_in_clickable else self._engine.arrow_cursor)

        self._show_upload_tooltip = False
        self._show_randomizer_tooltip = False
        self._show_erase_all_tooltip = False

        if self._upload_button.contains(mouse_pos):
            self._upload_tooltip.set_position(mouse_pos)
            self._show_upload_tooltip = True
            return

        if self._randomizer_button.contains(mouse_pos):
            self._randomizer_tooltip.set_position(mouse_pos)
            self._show_randomizer_tooltip = True
            return

        if self._erase_all_button.contains(mouse_pos):
            self._erase_all_tooltip.set_position(mouse_pos)
            self._show_erase_all_tooltip = True
            return

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self._nanogram_name.update_child_position()
        self._x_dimension.update_child_position()
        self._y_dimension.update_child_position()
        self._base.render(window)

        if self._show_upload_tooltip:
            self._upload_tooltip.render(window)

        if self._show_randomizer_tooltip:
            self._randomizer_tooltip.render(window)

        if self._show_erase_all_tooltip:
            self._erase_all_tooltip.render(window)

        if self._waiting_exit_confirmation:
            self._exit_message_popup.render(window)

            if time.time() - self._exit_time > 1:
                self._waiting_exit_confirmation = False
                from screens.workshop_screen import WorkshopScreen
                self._engine.set_screen(WorkshopScreen(self._engine))

        if self._showing_error_message:
            self._error_message_popup.render(window)

            if time.time() - self._error_start_time > 2:
                self._showing_error_message = False
                self._error_start_time = None
