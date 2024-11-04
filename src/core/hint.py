from core.types import rgb_t


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
