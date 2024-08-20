import pygame

from components.element import Element


class Text(Element):
    def __init__(self, text: str, font: pygame.font.Font, color: tuple[int, int, int]):
        self.text = text
        self.font = font
        self.color = color

        self.text_surface = self.font.render(self.text, True, self.color)
        width, height = self.text_surface.get_size()

        super().__init__(width, height)

        self.position = (0, 0)

    def render(self, window):
        window.blit(self.text_surface, self.position)

    """OPCIONES DE TEXTO"""

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    def set_position(self, position: tuple[int, int]):
        self.position = position

    def set_text(self, new_text: str):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.width, self.height = self.text_surface.get_size()

    def set_color(self, new_color: tuple[int, int, int]):
        self.color = new_color
        self.text_surface = self.font.render(self.text, True, self.color)

    def set_font(self, new_font: pygame.font.Font):
        self.font = new_font
        self.text_surface = self.font.render(self.text, True, self.color)
        self.width, self.height = self.text_surface.get_size()
