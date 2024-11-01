import pygame.image as image
from pygame import SurfaceType


class TextureManager:
    _BASE_DIR = "assets/textures/"

    @staticmethod
    def get(name: str) -> SurfaceType:
        return image.load(name)
