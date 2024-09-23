from typing import List, Tuple
import pygame
from typing import Self

from components.colored_block import ColoredBlock
from components import Column, Row, HorizontalAlignment, VerticalAlignment
from components.element import Element
from events import Event, EventType, MouseButton


class Colors(Element):
    def __init__(self, block_size: int, padding: int) -> None:
        cant_columns = 3
        cant_colors = 85

        super().__init__(cant_columns * (block_size + padding) - padding, cant_colors * (block_size + padding) - padding)
        self._block_size = block_size
        self._column1 = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column2 = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column3 = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column4 = Column().set_alignment(HorizontalAlignment.CENTER)
        self._column5 = Column().set_alignment(HorizontalAlignment.CENTER)

        colors = [
            (255, 0, 0),  # Rojo
            (255, 13, 0),  # Rojo claro
            (255, 26, 0),  # Rojo más claro
            (255, 38, 0),  # Rojo anaranjado
            (255, 51, 0),  # Naranja rojizo
            (255, 64, 0),  # Naranja
            (255, 77, 0),  # Naranja más claro
            (255, 89, 0),  # Naranja brillante
            (255, 102, 0),  # Naranja puro
            (255, 115, 0),  # Naranja amarillento
            (255, 128, 0),  # Naranja fuerte
            (255, 140, 0),  # Amarillo anaranjado
            (255, 153, 0),  # Amarillo suave
            (255, 166, 0),  # Amarillo más claro
            (255, 179, 0),  # Amarillo brillante
            (255, 191, 0),  # Amarillo intenso
            (255, 204, 0),  # Amarillo puro
            (255, 217, 0),  # Amarillo claro
            (255, 230, 0),  # Amarillo muy claro
            (255, 242, 0),  # Amarillo pálido
            (255, 255, 0),  # Amarillo blanco
            (242, 255, 13),  # Verde amarillento claro
            (230, 255, 26),  # Verde amarillento
            (217, 255, 38),  # Verde pálido
            (204, 255, 51),  # Verde brillante
            (191, 255, 64),  # Verde claro
            (179, 255, 77),  # Verde puro
            (166, 255, 89),  # Verde más claro
            (153, 255, 102),  # Verde suave
            (140, 255, 115),  # Verde celeste
            (128, 255, 128),  # Verde agua
            (115, 255, 140),  # Verde celeste brillante
            (102, 255, 153),  # Verde claro
            (89, 255, 166),  # Verde muy claro
            (77, 255, 179),  # Verde celeste suave
            (64, 255, 191),  # Celeste claro
            (51, 255, 204),  # Celeste brillante
            (38, 255, 217),  # Celeste puro
            (26, 255, 230),  # Celeste fuerte
            (13, 255, 242),  # Celeste claro
            (0, 255, 255),  # Celeste pálido
            (0, 242, 255),  # Azul claro
            (0, 230, 255),  # Azul brillante
            (0, 217, 255),  # Azul puro
            (0, 204, 255),  # Azul fuerte
            (0, 191, 255),  # Azul celeste
            (0, 179, 255),  # Azul más claro
            (0, 166, 255),  # Azul suave
            (0, 153, 255),  # Azul intenso
            (0, 140, 255),  # Azul brillante
            (0, 128, 255),  # Azul muy claro
            (0, 115, 255),  # Azul pálido
            (0, 102, 255),  # Azul suave
            (0, 89, 255),  # Azul-rosado
            (0, 77, 255),  # Azul fuerte
            (0, 64, 255),  # Azul brillante
            (0, 51, 255),  # Azul celeste
            (0, 38, 255),  # Azul puro
            (0, 26, 255),  # Azul claro
            (0, 13, 255),  # Azul muy claro
            (0, 0, 255),  # Azul brillante
            (26, 0, 255),  # Azul a morado
            (51, 0, 255),  # Morado claro
            (77, 0, 255),  # Morado puro
            (102, 0, 255),  # Morado intenso
            (128, 0, 255),  # Morado brillante
            (153, 0, 255),  # Morado celeste
            (179, 0, 255),  # Morado fuerte
            (204, 0, 255),  # Morado suave
            (230, 0, 255),  # Morado rojizo
            (255, 0, 255),  # Rosado claro
            (255, 0, 242),  # Rosado más oscuro
            (255, 0, 217),  # Rosado brillante
            (255, 0, 191),  # Rosado puro
            (255, 0, 166),  # Rosado fuerte
            (255, 0, 140),  # Rosado celeste
            (255, 0, 115),  # Rosado intenso
            (255, 0, 89),  # Rosado más oscuro
            (255, 0, 64),  # Rosado rojo
            (255, 0, 38),  # Rojo suave
            (255, 0, 13),  # Rojo brillante
            (255, 13, 0),  # Rojo claro
            (255, 26, 0),  # Rojo intermedio
            (255, 38, 0),  # Rojo más intenso
            (255, 51, 0),  # Rojo
        ]
        colors = colors[::-1]

        for color in colors:
            self._column1.add_element(ColoredBlock(block_size, color))
            self._column2.add_element(ColoredBlock(block_size, color))
            self._column3.add_element(ColoredBlock(block_size, color))
            self._column4.add_element(ColoredBlock(block_size, color))
            self._column5.add_element(ColoredBlock(block_size, color))
        self._row = Row().set_alignment(VerticalAlignment.CENTER).add_element(self._column1).add_element(self._column2).add_element(self._column3).add_element(self._column4).add_element(self._column5)


        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._row.set_position(position)
        return self

    def on_all_events(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        for column in self._row.elements:
            for block in column.elements:
                if block.contains(pygame.mouse.get_pos()):
                    b: ColoredBlock = block
                    color = b.color
                    return color


    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._row.render(screen)