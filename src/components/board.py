import pygame
from components.block import Block
from components.column import Column
from components.row import Row
from components.element import Element
from pygame.event import Event

class Board(Element):
    def __init__(self, dimension: int, size: int, separation: int):
        super().__init__(dimension, dimension)

        self.row = Row()
        for i in range(0,dimension):
            column = Column()
            for j in range(0,dimension):
                column.add_child(Block((size,size)))
            self.row.add_child(column)
            column.set_separation(separation)
        self.row.set_separation(separation)

        self.size = (self.row.get_size())
        print(self.size)
        self.position = (0, 0)


    """OPCIONES DE BOARD"""
    def set_position(self, new_position: tuple[int, int]):
        self.position = new_position
        self.row.set_position(self.position)

    def get_size(self) -> tuple[int, int]:
        return self.size



    """OPCIONES DE RENDER"""
    def render(self, window: pygame.Surface):
        self.row.render(window)


    """FUNCIONES DE COMPLEMENTARIAS"""
    def run_logic(self, event: Event) -> None:
        for columna in self.row.get_childs():
            for bloque in columna.get_childs():
                bloque.on_event(event)
