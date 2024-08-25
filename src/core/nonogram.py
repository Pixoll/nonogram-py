import json
from typing import Any, Literal, Self

from PIL import Image

type rgb_t = tuple[int, int, int]


class Nonogram:
    class Hint:
        _value: int
        _color: rgb_t

        def __init__(self, color: rgb_t):
            self._value = 1
            self._color = color

        def __repr__(self):
            br, bg, bb = self._color
            luminance = br * 0.2126 + bg * 0.7152 + bb * 0.0722
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
    _player_grid: list[list[rgb_t | Literal["x"] | None]]
    _used_colors: tuple[rgb_t, ...]
    _horizontal_hints: tuple[tuple[Hint, ...], ...]
    _vertical_hints: tuple[tuple[Hint, ...], ...]
    _size: tuple[int, int]
    _number_of_cells: int
    _correct_cells: int

    def __init__(self, nonogram: list[list[rgb_t | None]]):
        self._original = []
        self._player_grid = []
        self._correct_cells = 0

        for row in nonogram:
            self._original.append([])
            self._player_grid.append([])

            for color in row:
                if color is None or (
                        ((255 - color[0]) ** 2 + (255 - color[1]) ** 2 + (255 - color[2]) ** 2) ** 0.5) < 10:
                    self._original[-1].append(None)
                    self._correct_cells += 1
                else:
                    self._original[-1].append(color)

                self._player_grid[-1].append(None)

        self._horizontal_hints = tuple([Nonogram._get_hints(row) for row in self._original])
        self._vertical_hints = tuple([Nonogram._get_hints(column) for column in list(zip(*self._original))])
        self._size = (len(self._original[0]), len(self._original))
        self._number_of_cells = self._size[0] * self._size[1]
        used_colors = []

        for row in self._original:
            for color in row:
                if color is not None and color not in used_colors:
                    used_colors.append(color)

        self._used_colors = tuple(used_colors)

    @classmethod
    def from_pre_made(cls, id: int) -> Self:
        pre_made_nonogram: dict[str, Any] | None = None

        with open("../../nonograms/pre-made.json") as pre_made_nonograms:
            nonograms: list[dict[str, Any]] = json.load(pre_made_nonograms)
            for nonogram in nonograms:
                if nonogram["id"] == id:
                    pre_made_nonogram = nonogram
                    break

        if pre_made_nonogram is None:
            raise ValueError(f"No nonogram with id {id}")

        mask: str = pre_made_nonogram["mask"]
        width: int = pre_made_nonogram["width"]
        palette: dict[str, rgb_t] = {}

        for key, color_str in pre_made_nonogram["palette"].items():
            r1, r2, g1, g2, b1, b2 = color_str
            r = int(r1 + r2, 16)
            g = int(g1 + g2, 16)
            b = int(b1 + b2, 16)
            palette[key] = (r, g, b)

        nonogram_data: list[list[rgb_t | None]] = []

        for i in range(len(mask)):
            if i % width == 0:
                nonogram_data.append([])

            color = palette[mask[i]] if mask[i] in palette else None
            nonogram_data[-1].append(color)

        return cls(nonogram_data)

    @classmethod
    def from_image(cls, path: str, colors: int = 256, max_size: int = 100) -> Self:
        image = Image.open(path).convert("P", palette=Image.ADAPTIVE, colors=colors).convert("RGB")

        if image.width > max_size or image.height > max_size:
            factor = image.width / max_size if image.width > image.height else image.height / max_size
            image = image.resize((int(image.width / factor), int(image.height / factor)), Image.NEAREST)

        pixels = image.load()
        nonogram_data = []

        for i in range(image.height):
            nonogram_data.append([])
            for j in range(image.width):
                nonogram_data[i].append(pixels[j, i])

        return cls(nonogram_data)

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

    def __getitem__(self, index: tuple[int, int]) -> rgb_t | Literal["x"] | None:
        x, y = index
        return self._player_grid[y][x]

    def __setitem__(self, index: tuple[int, int], value: rgb_t | Literal["x"] | None) -> None:
        x, y = index
        if self._player_grid[y][x] == value:
            return

        self._player_grid[y][x] = value

        if value == "x":
            return

        if value == self._original[y][x]:
            self._correct_cells += 1
        else:
            self._correct_cells -= 1

    def __repr__(self):
        title = f"{Nonogram.__name__} {self._size[0]}x{self._size[1]}:"
        max_horizontal_hints = max(len(hints) for hints in self._horizontal_hints)
        max_vertical_hints = max(len(hints) for hints in self._vertical_hints)
        padding = "   "
        grid = ""

        for i in reversed(range(max_vertical_hints)):
            grid += padding * max_horizontal_hints
            for hints in self._vertical_hints:
                grid += hints[i].__repr__() if len(hints) > 0 and i < len(hints) else padding
            grid += "\n"

        for y in range(self._size[1]):
            hints = self._horizontal_hints[y]
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
                hints[-1]._value += 1
            else:
                hints.append(Nonogram.Hint(color))

            skipped = False

        return tuple(hints)[::-1]

    @staticmethod
    def run_test() -> None:
        a = (123, 48, 0)
        b = (163, 98, 9)
        c = (253, 198, 140)
        d = (0, 88, 36)
        e = (143, 198, 61)
        n = None

        nonogram_data = [
            [n, n, n, n, n, n, n, b, b, b, b, b, b, n, n, n],
            [n, n, n, n, n, n, b, b, b, b, b, b, b, b, b, n],
            [n, n, n, n, n, b, b, a, a, a, b, b, a, b, a, b],
            [n, n, n, n, n, b, c, c, c, c, a, a, b, a, b, a],
            [n, n, n, n, n, c, c, c, c, c, c, c, a, b, a, a],
            [n, n, n, n, n, n, c, c, n, n, n, c, c, a, a, a],
            [n, n, n, n, n, n, n, n, c, c, n, n, c, c, a, a],
            [n, n, n, n, n, n, n, c, c, c, c, n, n, c, a, n],
            [n, n, n, n, n, n, n, c, n, c, c, c, c, a, n, n],
            [n, n, d, n, n, n, c, c, n, c, c, n, n, n, n, n],
            [n, n, d, n, n, n, c, n, n, c, c, n, n, n, n, n],
            [n, n, d, d, n, c, c, n, c, c, c, n, n, n, n, n],
            [e, e, n, d, n, c, n, n, e, c, n, n, d, n, n, n],
            [n, e, e, n, d, c, n, c, e, c, n, e, d, n, n, n],
            [n, d, e, e, e, c, c, e, c, c, e, d, n, n, n, n],
            [e, e, d, d, e, e, e, e, e, d, n, n, n, n, n, n],
            [n, n, e, e, n, n, d, d, d, n, e, n, n, n, n, n],
            [n, e, e, n, n, n, n, n, n, n, n, n, n, n, n, n],
        ]

        nonogram = Nonogram(nonogram_data)
        nonogram._player_grid = nonogram_data
        print(nonogram)


Nonogram.run_test()
