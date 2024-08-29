import pygame
from components.area import Area
from components.element import Element
from pygame.event import Event
from events import Event, EventType, MouseButton


class Block(Element):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size[0], size[1])
        self.size = size
        self.surface = pygame.Surface(size)
        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)

        self.surface.fill(self.background_color)

        pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)

        self.position = (0, 0)
        self.child = None

        self.area = Area((self.width, self.height))
        self.align = "center"

        self.state = 0
        self.x_mark_visible = False  # Estado para la marca de "X"

        self.x_image = pygame.image.load('assets/textures/x.gif')
        self.x_image = pygame.transform.scale(self.x_image, (self.size[0], self.size[1]))


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

    def change_state(self, state: int):
        if state == 1:
            if self.state == 1:
                self.state = 0
                self.set_color((255, 255, 255))
            else:
                if self.state == 3:
                    self.toggle_x_mark()
                self.state = 1
                self.set_color((0, 0, 0))
        else:
            if self.state == 3:
                self.toggle_x_mark()
                self.state = 0
                self.set_color((255, 255, 255))
            else:
                self.state = 3
                self.set_color((255, 255, 255))
                self.toggle_x_mark()

    """OPCIONES DE RENDER"""
    def render(self, window: pygame.Surface):
        window.blit(self.surface, self.position)
        if self.child:
            self.child.render(window)

    def toggle_x_mark(self):
        if self.x_mark_visible:
            self.surface.fill(self.background_color)
            pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)
            self.x_mark_visible = False
        else:
            x_center = (self.surface.get_width() - self.x_image.get_width()) // 2
            y_center = (self.surface.get_height() - self.x_image.get_height()) // 2
            self.surface.blit(self.x_image, (x_center, y_center))
            pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 1)
            self.x_mark_visible = True

    def on_event(self, event: Event) -> None:
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
            mouse_pos = pygame.mouse.get_pos()

            if self.position[0] <= mouse_pos[0] <= self.position[0] + self.width and \
                    self.position[1] <= mouse_pos[1] <= self.position[1] + self.height:
                self.change_state(1)
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.RIGHT:
            mouse_pos = pygame.mouse.get_pos()

            if self.position[0] <= mouse_pos[0] <= self.position[0] + self.width and \
                    self.position[1] <= mouse_pos[1] <= self.position[1] + self.height:
                self.change_state(0)

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
