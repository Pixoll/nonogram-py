from components.element import Element


class Column(Element):
    def __init__(self):
        super().__init__(0, 0)
        self.elements = []
        self.position = (0, 0)
        self.update_size()

    """OPCIONES DE CONTAINER"""

    def add_child(self, element: Element):
        self.elements.append(element)
        self.update_size()
        self.__update_positions()

    def set_position(self, new_position: tuple[int, int]):
        self.position = new_position
        self.__update_positions()

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    """OPCIONES DE RENDER"""

    def render(self, window):
        for element in self.elements:
            element.render(window)

    """FUNCIONES COMPLEMENTARIAS"""

    def update_size(self):
        if not self.elements:
            self.width = 0
            self.height = 0
            return

        self.width = max(el.width for el in self.elements)
        self.height = sum(el.height for el in self.elements)

    def __update_positions(self):
        current_y = 0
        for element in self.elements:
            element_position = (self.position[0], self.position[1] + current_y)
            element.set_position(element_position)
            current_y += element.height
