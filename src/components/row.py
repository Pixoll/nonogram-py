from components.element import Element


class Row(Element):
    def __init__(self):
        super().__init__(0, 0)
        self.elements = []
        self.position = (0, 0)
        self.update_size()

    """OPCIONES DE ROW"""

    def add_child(self, element: Element):
        self.elements.append(element)
        self.update_size()

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    """OPCIONES DE RENDER"""

    def render(self, window):
        current_x = 0
        for element in self.elements:
            element.set_position((self.position[0] + current_x, self.position[1]))
            element.render(window)
            current_x += element.width

    """FUNCIONES DE COMPLEMENTARIAS"""

    def update_size(self):
        if not self.elements:
            self.width = 0
            self.height = 0
            return
        self.width = sum(el.width for el in self.elements)
        self.height = max(el.height for el in self.elements)

    def set_position(self, new_position: tuple[int, int]):
        self.position = new_position
        self.__update_positions()

    def __update_positions(self):
        current_x = 0
        for element in self.elements:
            element.set_position((self.position[0] + current_x, self.position[1]))
            current_x += element.width
