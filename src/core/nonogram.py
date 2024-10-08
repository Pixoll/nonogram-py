import json
import os.path as path
from os import listdir, makedirs
from random import randrange
from typing import Any, Literal, Self

from PIL import Image

rgb_t = tuple[int, int, int]
nonogram_type_t = Literal["pre_made", "image", "custom", "generated"]


class Nonogram:
    class Hint:
        _value: int
        _color: rgb_t

        def __init__(self, color: rgb_t):
            self._value = 1
            self._color = color

        def __repr__(self):
            br, bg, bb = self._color
            luminance = Nonogram._get_color_luminance(self._color)
            fr, fg, fb = (255, 255, 255) if luminance < 140 else (0, 0, 0)
            value_str = (
                f" {self._value} " if self._value < 10
                else f" {self._value}" if self._value < 100
                else "100")
            return f"\033[48;2;{br};{bg};{bb}m\033[38;2;{fr};{fg};{fb}m{value_str}\033[0m"

        @property
        def value(self) -> int:
            return self._value

        @property
        def color(self) -> rgb_t:
            return self._color

    _original: list[list[rgb_t | None]]
    _original_transposed: list[list[rgb_t | None]]
    _player_grid: list[list[rgb_t | Literal["x"] | None]]
    _player_grid_transposed: list[list[rgb_t | Literal["x"] | None]]
    _palette: dict[str, rgb_t]
    _used_colors: tuple[rgb_t, ...]
    _horizontal_hints: tuple[tuple[Hint, ...], ...]
    _vertical_hints: tuple[tuple[Hint, ...], ...]
    _size: tuple[int, int]
    _number_of_cells: int
    _correct_cells: int
    _type: nonogram_type_t
    _id: int | None

    def __init__(
            self,
            nonogram: list[list[rgb_t | None]],
            nonogram_type: nonogram_type_t,
            nonogram_id: int | None = None,
            palette: dict[str, rgb_t] | None = None,
    ):
        self._original = []
        self._player_grid = []
        self._correct_cells = 0

        used_colors: dict[rgb_t, int] = {}

        for row in nonogram:
            self._original.append([])
            self._player_grid.append([])

            for color in row:
                if nonogram_type == "pre_made":
                    self._original[-1].append(color)

                    if color is None:
                        self._correct_cells += 1
                    else:
                        if color not in used_colors:
                            used_colors[color] = 1
                        else:
                            used_colors[color] += 1

                    self._player_grid[-1].append(None)
                    continue

                if color is None or color == (255, 255, 255):
                    self._original[-1].append(None)
                    self._correct_cells += 1
                else:
                    self._original[-1].append(color)

                    if color not in used_colors:
                        used_colors[color] = 1
                    else:
                        used_colors[color] += 1

                self._player_grid[-1].append(None)

        if nonogram_type == "image" and nonogram_id is None and len(used_colors) > 1:
            lightest_color: rgb_t | None = None
            highest_luminance = 0

            for color in used_colors:
                luminance = Nonogram._get_color_luminance(color)
                if luminance > 200 and luminance > highest_luminance:
                    highest_luminance = luminance
                    lightest_color = color

            if lightest_color is not None:
                for row in self._original:
                    for i in range(len(row)):
                        if row[i] == lightest_color:
                            row[i] = None

            del used_colors[lightest_color]

        if palette is None:
            palette = {}
            i = 0
            for color in used_colors.keys():
                palette[str(i)] = color
                i += 1

        self._palette = palette
        self._original_transposed = list([list(column) for column in zip(*self._original)])
        self._player_grid_transposed = list([list(column) for column in zip(*self._player_grid)])
        self._horizontal_hints = tuple([Nonogram._get_hints(row) for row in self._original])
        self._vertical_hints = tuple([Nonogram._get_hints(column) for column in self._original_transposed])
        self._size = (len(self._original[0]), len(self._original))
        self._number_of_cells = self._size[0] * self._size[1]
        self._type = nonogram_type
        self._id = nonogram_id
        # noinspection PyTypeChecker
        self._used_colors = tuple(palette.values())

    @classmethod
    def from_pre_made(cls, nonogram_id: int) -> Self:
        nonogram_path = f"nonograms/pre_made/{nonogram_id}.json"

        if not path.exists(nonogram_path):
            raise ValueError(f"No nonogram with id {nonogram_id}")

        pre_made_nonogram: dict[str, Any]
        with open(nonogram_path) as nonogram_file:
            pre_made_nonogram = json.load(nonogram_file)

        mask: str = pre_made_nonogram["mask"]
        width: int = pre_made_nonogram["width"]
        palette = Nonogram._get_palette(pre_made_nonogram["palette"])

        nonogram_data: list[list[rgb_t | None]] = []

        for i in range(len(mask)):
            if i % width == 0:
                nonogram_data.append([])

            color = palette[mask[i]] if mask[i] in palette else None
            nonogram_data[-1].append(color)

        nonogram = cls(nonogram_data, "pre_made", nonogram_id, palette)

        return nonogram

    @classmethod
    def from_image(cls, image_path: str, colors: int = 256, max_size: int = 100) -> Self:
        image = Image.open(image_path).convert("P", palette=Image.ADAPTIVE, colors=colors).convert("RGB")

        if image.width > max_size or image.height > max_size:
            factor = image.width / max_size if image.width > image.height else image.height / max_size
            image = image.resize((int(image.width / factor), int(image.height / factor)), Image.NEAREST)

        pixels = image.load()
        nonogram_data = []

        for i in range(image.height):
            nonogram_data.append([])
            for j in range(image.width):
                nonogram_data[i].append(pixels[j, i])

        return cls(nonogram_data, "image")

    @classmethod
    def generate(cls, size: tuple[int, int], colors: list[rgb_t] | None = None) -> Self:
        if colors is None:
            colors = [(0, 0, 0)]

        test = set()
        nonogram_data: list[list[rgb_t | None]] = []
        total_colors = size[0] * size[1] * randrange(30, 70) / 100
        colored = 0

        for i in range(size[0]):
            nonogram_data.append([])
            for j in range(size[1]):
                nonogram_data[i].append(None)

        while colored < total_colors:
            x = randrange(0, size[0])
            y = randrange(0, size[1])
            if nonogram_data[x][y] is None:
                index = randrange(len(colors))
                test.add(index)
                color = colors[index]
                nonogram_data[x][y] = color
                colored += 1

        return cls(nonogram_data, "generated")

    @classmethod
    def load(cls, nonogram_type: nonogram_type_t, nonogram_id: int) -> Self:
        nonogram_path = f"nonograms/{nonogram_type}/{nonogram_id}.json"
        if not path.exists(nonogram_path):
            raise ValueError(f"No nonogram of type {nonogram_type} with id {nonogram_id}")

        nonogram_json: Any
        with open(nonogram_path) as nonogram_file:
            nonogram_json = json.load(nonogram_file)

        if nonogram_json["player_mask"] is None:
            raise ValueError(f"Nonogram of type {nonogram_type} with id {nonogram_id} hasn't been played before")

        if nonogram_json["completed"]:
            raise ValueError(f"Nonogram of type {nonogram_type} with id {nonogram_id} has already been completed")

        width: int = nonogram_json["width"]
        mask: str = nonogram_json["mask"]
        player_mask: str = nonogram_json["player_mask"]
        palette = Nonogram._get_palette(nonogram_json["palette"])
        el_len = max([len(k) for k in palette.keys()])

        nonogram_data: list[list[rgb_t | None]] = []
        player_grid: list[list[rgb_t | Literal["x"] | None]] = []

        for i in range(0, len(mask), el_len):
            if i % (width * el_len) == 0:
                nonogram_data.append([])
                player_grid.append([])

            original_mask_element = (str(int(mask[i:i + el_len]))
                                     if mask[i:i + el_len].isdigit()
                                     else mask[i:i + el_len])
            player_mask_element = (str(int(player_mask[i:i + el_len]))
                                   if player_mask[i:i + el_len].isdigit()
                                   else player_mask[i:i + el_len])

            nonogram_data[-1].append(
                palette[original_mask_element] if original_mask_element in palette
                else None
            )
            player_grid[-1].append(
                palette[player_mask_element] if player_mask_element in palette
                else "x" if player_mask[i:i + el_len][0] == "x"
                else None
            )

        nonogram = cls(nonogram_data, nonogram_type, nonogram_id, palette)
        nonogram._player_grid = player_grid

        return nonogram

    @property
    def used_colors(self) -> tuple[rgb_t, ...]:
        return self._used_colors

    @property
    def horizontal_hints(self) -> tuple[tuple[Hint, ...], ...]:
        return self._horizontal_hints

    @property
    def vertical_hints(self) -> tuple[tuple[Hint, ...], ...]:
        return self._vertical_hints

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def is_completed(self) -> bool:
        return self._correct_cells == self._number_of_cells

    def is_row_complete(self, row: int) -> bool:
        return self._player_grid[row] == self._original[row]

    def is_column_complete(self, column: int) -> bool:
        return self._player_grid_transposed[column] == self._original_transposed[column]

    def save(self) -> None:
        save_path = f"nonograms/{self._type}/"

        el_len = max([len(k) for k in self._palette.keys()])
        inverse_palette: dict[rgb_t, str] = {v: k for k, v in self._palette.items()}

        # noinspection PyTypeChecker
        player_mask = "".join(["".join([
            " " * el_len if color is None
            else "x" * el_len if color == "x"
            else inverse_palette[color].zfill(el_len) for color in row
        ]) for row in self._player_grid])

        if self._id is not None:
            pre_made_nonogram: Any

            with open(save_path + f"/{self._id}.json") as nonogram_file:
                pre_made_nonogram = json.load(nonogram_file)

            pre_made_nonogram["player_mask"] = player_mask
            pre_made_nonogram["completed"] = self.is_completed

            with open(save_path + f"/{self._id}.json", "w") as nonogram_file:
                json.dump(pre_made_nonogram, nonogram_file, indent=2)

            return

        if not path.exists(save_path):
            makedirs(save_path)

        saved_nonograms = listdir(save_path)
        nonogram_id = int(saved_nonograms[-1].split(".")[0]) + 1 if len(saved_nonograms) > 0 else 1

        pre_made_nonogram = {
            "id": nonogram_id,
            "mask": "".join(["".join([
                " " * el_len if color is None
                else inverse_palette[color].zfill(el_len) for color in row
            ]) for row in self._original]),
            "width": self._size[0],
            "height": self._size[1],
            "palette": {k: "%02x%02x%02x" % v for k, v in self._palette.items()},
            "player_mask": None if player_mask.strip() == "" else player_mask,
            "completed": self.is_completed,
        }

        with open(save_path + f"/{nonogram_id}.json", "w") as nonogram_file:
            json.dump(pre_made_nonogram, nonogram_file, indent=2)

    def __getitem__(self, index: tuple[int, int]) -> rgb_t | Literal["x"] | None:
        x, y = index
        return self._player_grid[y][x]

    def __setitem__(self, index: tuple[int, int], new_value: rgb_t | Literal["x"] | None) -> None:
        x, y = index
        if self._player_grid[y][x] == new_value:
            return

        old_value = self._player_grid[y][x]
        is_old_correct = (None if old_value == "x" else old_value) == self._original[y][x]
        is_new_correct = (None if new_value == "x" else new_value) == self._original[y][x]

        self._player_grid[y][x] = new_value
        self._player_grid_transposed[x][y] = new_value

        if is_old_correct == is_new_correct:
            return

        self._correct_cells += 1 if is_new_correct else -1

    def __repr__(self):
        title = f"{Nonogram.__name__} {self._size[0]}x{self._size[1]}:"
        max_horizontal_hints = max(len(hints) for hints in self._horizontal_hints)
        max_vertical_hints = max(len(hints) for hints in self._vertical_hints)
        padding = "   "
        grid = ""

        for i in reversed(range(max_vertical_hints)):
            grid += padding * max_horizontal_hints
            for hints in self._vertical_hints:
                hints = hints[::-1]
                grid += hints[i].__repr__() if len(hints) > 0 and i < len(hints) else padding
            grid += "\n"

        for y in range(self._size[1]):
            hints = self._horizontal_hints[y][::-1]
            for i in reversed(range(max_horizontal_hints)):
                grid += hints[i].__repr__() if len(hints) > 0 and i < len(hints) else padding

            for x in range(self._size[0]):
                cell = self._player_grid[y][x]

                if cell is None:
                    grid += padding
                elif cell == "x":
                    grid += f"\033[38;2;255;64;64m X \033[0m"
                else:
                    grid += f"\033[48;2;{cell[0]};{cell[1]};{cell[2]}m{padding}\033[0m"

            grid += "\n"

        return title + "\n" + grid

    @staticmethod
    def _get_hints(row_or_column: list[rgb_t]) -> tuple[Hint, ...]:
        hints: list[Nonogram.Hint] = []
        skipped: bool = False

        for color in row_or_column:
            if color is None:
                skipped = True
                continue

            if len(hints) == 0:
                hints.append(Nonogram.Hint(color))
                skipped = False
                continue

            if hints[-1].color == color and not skipped:
                # noinspection PyProtectedMember
                hints[-1]._value += 1
            else:
                hints.append(Nonogram.Hint(color))

            skipped = False

        return tuple(hints)

    @staticmethod
    def _get_palette(palette_json: dict[str, str]) -> dict[str, rgb_t]:
        palette: dict[str, rgb_t] = {}

        for key, color_str in palette_json.items():
            r1, r2, g1, g2, b1, b2 = color_str
            r = int(r1 + r2, 16)
            g = int(g1 + g2, 16)
            b = int(b1 + b2, 16)
            palette[key] = (r, g, b)

        return palette

    @staticmethod
    def _get_color_luminance(color: rgb_t) -> float:
        r, g, b = color
        return r * 0.2126 + g * 0.7152 + b * 0.0722
