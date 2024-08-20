import pygame
from src.components.area import Area
from src.components.element import Element


class Container(Element):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size[0], size[1])
        self.size = size
        self.surface = pygame.Surface(size)
        self.background_color = (255, 255, 255)
        self.border_color = (255, 255, 255)

        self.surface.fill(self.background_color)

        pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)

        self.position = (0, 0)
        self.child = None

        self.area = Area((self.width, self.height))
        self.align = "center"

    """OPCIONES DE CONTAINER"""

    def set_color(self, new_color: tuple[int, int, int]):
        self.background_color = new_color
        self.surface.fill(self.background_color)
        pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)

    def set_border(self, border_color: tuple[int, int, int]):
        self.border_color = border_color
        pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)

    def set_position(self, new_position: tuple[int, int]):
        self.position = new_position
        self.__update_position()

    def set_child(self, child_container):
        self.child = child_container
        self.__update_position()

    def get_size(self) -> tuple[int, int]:
        return self.size

    def alignment(self, alignment: str):
        if alignment in [
            "center", "topCenter", "bottomCenter",
            "topRight", "bottomRight", "topLeft", "bottomLeft",
            "centerRight", "centerLeft"
        ]:
            self.align = alignment
            self.__update_position()

    """OPCIONES DE RENDER"""

    def render(self, window: pygame.Surface):
        window.blit(self.surface, self.position)
        if self.child:
            self.child.render(window)

    """FUNCIONES COMPLEMENTARIA"""

    def __update_position(self):
        if self.child:
            obj_size = self.child.get_size()
            if self.align == "center":
                aux = self.area.center(obj_size)
            elif self.align == "topCenter":
                aux = self.area.top_center(obj_size)
            elif self.align == "bottomCenter":
                aux = self.area.bottom_center(obj_size)
            elif self.align == "topRight":
                aux = self.area.top_right(obj_size)
            elif self.align == "bottomRight":
                aux = self.area.bottom_right(obj_size)
            elif self.align == "topLeft":
                aux = self.area.top_left(obj_size)
            elif self.align == "bottomLeft":
                aux = self.area.bottom_left(obj_size)
            elif self.align == "centerRight":
                aux = self.area.center_right(obj_size)
            elif self.align == "centerLeft":
                aux = self.area.center_left(obj_size)
            child_position = (aux[0] + self.position[0], aux[1] + self.position[1])
            self.child.set_position(child_position)
