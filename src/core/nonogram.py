from random import randrange
from typing import Literal, Sequence

from PIL import Image

from core.hint import Hint
from core.types import nonogram_matrix_t, nonogram_type_t, rgb_t


class Nonogram:
    _original: nonogram_matrix_t
    _player_grid: list[list[rgb_t | Literal["x"] | None]]
    _palette: dict[str, rgb_t]
    _used_colors: tuple[rgb_t, ...]
    _horizontal_hints: list[list[Hint]]
    _vertical_hints: list[list[Hint]]
    _size: tuple[int, int]
    _number_of_cells: int
    _correct_cells: int
    _type: nonogram_type_t
    _id: int | None
    _name: str | None

    def __init__(
            self,
            nonogram: nonogram_matrix_t,
            nonogram_type: nonogram_type_t,
            nonogram_id: int | None = None,
            nonogram_name: str | None = None,
            palette: dict[str, rgb_t] | None = None,
    ):
        self._original = []
        self._player_grid = []
        self._horizontal_hints = []
        self._correct_cells = 0
        self._size = (len(nonogram[0]), len(nonogram))
        self._number_of_cells = self._size[0] * self._size[1]
        self._type = nonogram_type
        self._id = nonogram_id
        self._name = nonogram_name

        used_colors: set[rgb_t] = set()

        for row in nonogram:
            self._original.append([])
            self._player_grid.append([])

            for color in row:
                if color is None or color == (255, 255, 255):
                    self._original[-1].append(None)
                    self._correct_cells += 1
                else:
                    self._original[-1].append(color)
                    used_colors.add(color)

                self._player_grid[-1].append(None)

            self._horizontal_hints.append(Nonogram._get_hints(row))

        if len(used_colors) > 128:
            raise ValueError("Nonogram cannot have more than 128 colors.")

        if palette is not None:
            self._palette = palette
        else:
            self._palette = {}
            i = 1
            for color in used_colors:
                self._palette[str(i)] = color
                i += 1

        self._vertical_hints = [Nonogram._get_hints(column) for column in zip(*self._original)]
        self._used_colors = tuple(used_colors)

    @staticmethod
    def matrix_from_image(
            image_path: str,
            colors: int = 128,
            size: tuple[int, int] = (0, 0),
            delete_lightest: bool = False
    ) -> nonogram_matrix_t:
        if colors > 128:
            raise ValueError("Nonogram cannot have more than 128 colors.")

        image = Image.open(image_path).convert("P", palette=Image.ADAPTIVE, colors=colors).convert("RGB")

        if size[0] != 0 and size[1] != 0:
            image = image.resize(size, Image.NEAREST)

        pixels = image.load()
        nonogram_data: nonogram_matrix_t = []
        used_colors: set[rgb_t] = set()

        for i in range(image.height):
            nonogram_data.append([])
            for j in range(image.width):
                # noinspection PyTypeChecker
                color: rgb_t = pixels[j, i]
                used_colors.add(color)
                nonogram_data[i].append(color)

        if delete_lightest and len(used_colors) > 1:
            lightest_color: rgb_t | None = None
            highest_luminance = 0

            for color in used_colors:
                r, g, b = color
                luminance = r * 0.2126 + g * 0.7152 + b * 0.0722
                if luminance > 200 and luminance > highest_luminance:
                    highest_luminance = luminance
                    lightest_color = color

            if lightest_color is not None:
                for row in nonogram_data:
                    for i in range(len(row)):
                        if row[i] == lightest_color:
                            row[i] = None

        return nonogram_data

    @staticmethod
    def matrix_randomized(size: tuple[int, int], colors: list[rgb_t] | None = None) -> nonogram_matrix_t:
        if colors is None:
            colors = [(0, 0, 0)]

        if len(colors) > 128:
            raise ValueError("Nonogram cannot have more than 128 colors.")

        nonogram_data: nonogram_matrix_t = []
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
                color = colors[index]
                nonogram_data[x][y] = color
                colored += 1

        return nonogram_data

    @property
    def used_colors(self) -> tuple[rgb_t, ...]:
        return self._used_colors

    @property
    def horizontal_hints(self) -> Sequence[Sequence[Hint]]:
        return self._horizontal_hints

    @property
    def vertical_hints(self) -> Sequence[Sequence[Hint]]:
        return self._vertical_hints

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def name(self) -> str | None:
        return self._name

    @property
    def is_completed(self) -> bool:
        return self._correct_cells == self._number_of_cells

    def is_row_complete(self, row: int) -> bool:
        for x in range(self._size[0]):
            cell = self._player_grid[row][x]
            if (None if cell == "x" else cell) != self._original[row][x]:
                return False
        return True

    def is_column_complete(self, column: int) -> bool:
        for y in range(self._size[1]):
            cell = self._player_grid[y][column]
            if (None if cell == "x" else cell) != self._original[y][column]:
                return False
        return True

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

        if is_old_correct == is_new_correct:
            return

        self._correct_cells += 1 if is_new_correct else -1

    def __repr__(self):
        title = f"{Nonogram.__name__} \"{self._name or "[NO_NAME]"}\" {self._size[0]}x{self._size[1]}:"
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
                    grid += f"\033[48;2;255;255;255m{padding}\033[0m"
                elif cell == "x":
                    grid += f"\033[38;2;255;64;64m X \033[0m"
                else:
                    grid += f"\033[48;2;{cell[0]};{cell[1]};{cell[2]}m{padding}\033[0m"

            grid += "\n"

        return title + "\n" + grid

    @staticmethod
    def _get_hints(row_or_column: Sequence[rgb_t]) -> list[Hint]:
        hints: list[Hint] = []
        skipped: bool = False

        for color in row_or_column:
            if color is None:
                skipped = True
                continue

            if len(hints) == 0:
                hints.append(Hint(color))
                skipped = False
                continue

            if hints[-1].color == color and not skipped:
                # noinspection PyProtectedMember
                hints[-1]._value += 1
            else:
                hints.append(Hint(color))

            skipped = False

        return hints
