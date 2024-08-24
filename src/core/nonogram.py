from typing import Literal, Self

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
            value_str = (f" {self._value} " if self._value < 10
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

    def __init__(self, nonogram: list[list[rgb_t | None]]):
        self._original = [
            [None if (((255 - r) ** 2 + (255 - g) ** 2 + (255 - b) ** 2) ** 0.5) < 10 else (r, g, b) for r, g, b in row]
            for row in nonogram
        ]
        self._player_grid = [[None for _ in range(len(self._original[0]))] for _ in range(len(self._original))]
        self._horizontal_hints = tuple([Nonogram._get_hints(row) for row in self._original])
        self._vertical_hints = tuple([Nonogram._get_hints(column) for column in list(zip(*self._original))])
        self._size = (len(self._original[0]), len(self._original))
        used_colors = []

        for row in self._original:
            for color in row:
                if color is not None and color not in used_colors:
                    used_colors.append(color)

        self._used_colors = tuple(used_colors)

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

    def __getitem__(self, index: tuple[int, int]) -> rgb_t | Literal["x"] | None:
        x, y = index
        return self._player_grid[y][x]

    def __setitem__(self, index: tuple[int, int], value: rgb_t | Literal["x"] | None) -> None:
        x, y = index
        self._player_grid[y][x] = value

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
