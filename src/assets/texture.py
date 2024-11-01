import pygame.image as image
import pygame.transform as transform
from pygame import SurfaceType


class TextureManager:
    _BASE_DIR = "assets/textures/"

    _TEXTURES: dict[tuple[str, tuple[int, int] | None], SurfaceType] = {}

    @staticmethod
    def get(name: str, size: tuple[int, int] | None = None) -> SurfaceType:
        if (name, None) not in TextureManager._TEXTURES:
            texture = image.load(TextureManager._BASE_DIR + name)
            TextureManager._TEXTURES[(name, None)] = texture
            TextureManager._TEXTURES[(name, texture.get_size())] = texture

        if size is not None and (name, size) not in TextureManager._TEXTURES:
            base_texture = TextureManager._TEXTURES[(name, None)]
            TextureManager._TEXTURES[(name, size)] = transform.scale(base_texture, size)

        return TextureManager._TEXTURES[(name, size)]
