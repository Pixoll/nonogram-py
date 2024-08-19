type rgb_t = tuple[int, int, int]
type nonogram_t = list[list[rgb_t | None]]


class Hint:
    value: int
    color: rgb_t

    def __init__(self, color: rgb_t):
        self.value = 1
        self.color = color

    def __repr__(self):
        return f'Hint({self.value}, {self.color})'


class Game:
    original_nonogram: nonogram_t
    used_colors: list[rgb_t]
    horizontal_hints: list[list[Hint]]
    vertical_hints: list[list[Hint]]

    def __init__(self, nonogram: nonogram_t):
        self.original_nonogram = nonogram
        self.horizontal_hints = [Game._get_hints(row) for row in nonogram]
        self.vertical_hints = [Game._get_hints(column) for column in list(zip(*nonogram))]
        self.used_colors = []

        for row in nonogram:
            for color in row:
                if color is not None and color not in self.used_colors:
                    self.used_colors.append(color)

    @staticmethod
    def _get_hints(row_or_column: list[rgb_t]) -> list[Hint]:
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
                hints[-1].value += 1
            else:
                hints.append(Hint(color))

            skipped = False

        return hints
