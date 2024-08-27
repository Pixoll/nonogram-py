from components import Element

class Column(Element):
    def __init__(self):
        super().__init__(0, 0)
        self.elements = []
        self.position = (0, 0)
        self.__update_size()
        self.separation = 0

        self.maxWidth = 0
        self.align = "center"

    """OPCIONES DE COLUMN"""
    def add_child(self, element: Element):
        self.elements.append(element)
        self.__update_size()
        self.__update_positions()

    def set_position(self, new_position: tuple[int, int]):
        self.position = new_position
        self.__update_positions()

    def set_separation(self, val: int):
        self.separation = val
        self.__update_positions()
        self.__update_size()

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    def get_childs(self) -> list[Element]:
        return self.elements

    def alignment(self, alignment: str):
        if alignment in [
            "center", "left", "right"
        ]:
            self.align = alignment
            self.__update_positions()

    """OPCIONES DE RENDER"""
    def render(self, window):
        for element in self.elements:
            element.render(window)


    """FUNCIONES COMPLEMENTARIAS"""
    def __update_size(self):
        if not self.elements:
            self.width = 0
            self.height = 0
            return
        self.width = max(el.width for el in self.elements)
        self.maxWidth = self.width
        self.height = sum(el.height for el in self.elements) + self.separation*(len(self.elements)-1)

    def __update_positions(self):
        current_y = 0
        for element in self.elements:
            if self.align == "center":
                align = (self.maxWidth - element.get_size()[0]) / 2
            elif self.align == "left":
                align = 0
            else:
                align = (self.maxWidth - element.get_size()[0])
            element_position = (self.position[0] +  align, self.position[1] + current_y)
            element.set_position(element_position)
            current_y += element.height + self.separation