from typing import Literal

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
            return f"{Nonogram.Hint.__name__} \033[48;2;{br};{bg};{bb}m\033[38;2;{fr};{fg};{fb}m {self._value} \033[0m"

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
        self._original = nonogram
        self._player_grid = [[None for _ in range(len(nonogram[0]))] for _ in range(len(nonogram))]
        self._horizontal_hints = tuple([Nonogram._get_hints(row) for row in nonogram])
        self._vertical_hints = tuple([Nonogram._get_hints(column) for column in list(zip(*nonogram))])
        self._size = (len(nonogram[0]), len(nonogram))
        used_colors = []

        for row in nonogram:
            for color in row:
                if color is not None and color not in used_colors:
                    used_colors.append(color)

        self._used_colors = tuple(used_colors)

    def __repr__(self):
        title = f"{Nonogram.__name__} {self._size[0]}x{self._size[1]}:"
        max_horizontal_hints = max(len(hints) for hints in self._horizontal_hints)
        max_vertical_hints = max(len(hints) for hints in self._vertical_hints)
        grid = ""

        for i in reversed(range(max_vertical_hints)):
            grid += " " * max_horizontal_hints * 3

            for hints in self._vertical_hints:
                if len(hints) > 0 and i < len(hints):
                    grid += hints[i].__repr__().replace(Nonogram.Hint.__name__ + " ", "")
                else:
                    grid += "   "

            grid += "\n"

        for y in range(self._size[1]):
            hints = self._horizontal_hints[y]
            for i in reversed(range(max_horizontal_hints)):
                if len(hints) > 0 and i < len(hints):
                    grid += hints[i].__repr__().replace(Nonogram.Hint.__name__ + " ", "")
                else:
                    grid += "   "

            for x in range(self._size[0]):
                cell = self._player_grid[y][x]

                if cell is None:
                    grid += "   "
                elif cell == "x":
                    grid += f"\033[38;2;255;64;64m X \033[0m"
                else:
                    grid += f"\033[48;2;{cell[0]};{cell[1]};{cell[2]}m   \033[0m"

            grid += "\n"

        return title + "\n" + grid

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
        self._assert_bounds(x, y)
        return self._player_grid[y][x]

    def set_cross(self, x: int, y: int) -> None:
        self._assert_bounds(x, y)
        self._player_grid[y][x] = "x"

    def set_color(self, x: int, y: int, color: rgb_t) -> None:
        self._assert_bounds(x, y)
        self._player_grid[y][x] = color

    def set_none(self, x: int, y: int) -> None:
        self._assert_bounds(x, y)
        self._player_grid[y][x] = None

    def _assert_bounds(self, x: int, y: int) -> None:
        if x < 0 or y < 0 or x >= self._size[0] or y >= self._size[1]:
            print("what are you doing")
            exit(1)

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
