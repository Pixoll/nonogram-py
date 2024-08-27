from components.element import Element

class Row(Element):
    def __init__(self):
        super().__init__(0, 0)
        self.elements = []
        self.position = (0, 0)
        self.__update_size()
        self.separation = 0

        self.maxHeigth = 0
        self.align = "center"

    """OPCIONES DE ROW"""
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
            "center", "top", "bottom"
        ]:
            self.align = alignment
            self.__update_positions()

    """OPCIONES DE RENDER"""
    def render(self, window):
        for element in self.elements:
            element.render(window)


    """FUNCIONES DE COMPLEMENTARIAS"""
    def __update_size(self):
        if not self.elements:
            self.width = 0
            self.height = 0
            return
        self.width = sum(el.width for el in self.elements) + self.separation*(len(self.elements)-1)
        self.height = max(el.height for el in self.elements)
        self.maxHeigth = self.height

    def __update_positions(self):
        current_x = 0
        for element in self.elements:
            if self.align == "center":
                align = (self.maxHeigth - element.get_size()[1]) / 2
            elif self.align == "top":
                align = 0
            else:
                align = (self.maxHeigth - element.get_size()[1])
            element_position = (self.position[0] + current_x, self.position[1] + align)
            element.set_position(element_position)
            current_x += element.width + self.separation