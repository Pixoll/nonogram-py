from typing import Literal

from pygame.font import Font, match_font


class FontFormat:
    FAKE_BOLD = 0b0001
    FAKE_ITALIC = 0b0010
    UNDERLINE = 0b0100
    STRIKETHROUGH = 0b1000

    @staticmethod
    def parse(flags: int) -> tuple[bool, bool, bool, bool]:
        bold = bool(flags & FontFormat.FAKE_BOLD)
        italic = bool(flags & FontFormat.FAKE_ITALIC)
        underline = bool(flags & FontFormat.UNDERLINE)
        strikethrough = bool(flags & FontFormat.STRIKETHROUGH)
        return bold, italic, underline, strikethrough


class FontManager:
    _BASE_DIR = "assets/fonts/"
    _DEFAULT_FONT_PATH = _BASE_DIR + "PixeloidSans.ttf"

    class _FontAsset:
        _path: str | None
        _size: int
        _formats: dict[tuple[bool, bool, bool, bool], Font]

        def __init__(self, path: str | None, size: int, flags: int = 0):
            self._path = path
            self._size = size
            self._formats = {}

            parsed_flags = FontFormat.parse(flags)
            self._formats[parsed_flags] = FontManager._FontAsset._load(path, size, *parsed_flags)

        def get(self, flags: int = 0) -> Font:
            parsed_flags = FontFormat.parse(flags)
            if parsed_flags not in self._formats:
                self._formats[parsed_flags] = FontManager._FontAsset._load(self._path, self._size, *parsed_flags)

            return self._formats[parsed_flags]

        @staticmethod
        def _load(path: str | None, size: int, bold: bool, italic: bool, underline: bool, strikethrough: bool) -> Font:
            font = Font(path, size)
            font.set_bold(bold)
            font.set_italic(italic)
            font.set_underline(underline)
            font.set_strikethrough(strikethrough)
            return font

    _FONTS: dict[tuple[str | None, int], _FontAsset] = {}

    @staticmethod
    def get(font_type: Literal["local", "sys"], name: str | None, size: int, flags: int = 0) -> Font:
        path = FontManager._resolve_path(font_type, name, flags)
        font_key = (path, size)

        if font_key not in FontManager._FONTS:
            FontManager._FONTS[font_key] = FontManager._FontAsset(path, size, flags)

        return FontManager._FONTS[font_key].get(flags)

    @staticmethod
    def get_default(size: int, flags: int = 0) -> Font:
        font_key = (FontManager._DEFAULT_FONT_PATH, size)

        if font_key not in FontManager._FONTS:
            FontManager._FONTS[font_key] = FontManager._FontAsset(FontManager._DEFAULT_FONT_PATH, size, flags)

        return FontManager._FONTS[font_key].get(flags)

    @staticmethod
    def _resolve_path(font_type: Literal["local", "sys"], name: str | None, flags: int = 0) -> str | None:
        if name is None:
            return None

        path: str

        if font_type == "sys":
            bold = bool(flags & FontFormat.FAKE_BOLD)
            italic = bool(flags & FontFormat.FAKE_ITALIC)
            path = match_font(name, bold, italic)

            if path is None:
                raise ValueError(f"Could not find system font '{name}'")
        else:
            path = FontManager._BASE_DIR + name

        return path
