from typing import Self
import pygame
from components.element import Element
from components.colored_block import ColoredBlock
from components import Column
from events import Event, EventType, MouseButton

class RecentColors(Element):
    def __init__(self, block_size: int, padding: int) -> None:
        # Ajustar el tamaño del contenedor para acomodar 6 bloques verticales
        super().__init__(block_size, block_size * 6 + padding * 5)
        self._block_size = block_size
        self._padding = padding
        self._current_color = (255, 255, 255)
        self._recent_colors = [(255, 255, 255) for _ in range(6)]  # Inicia con seis bloques blancos

        # Crear una columna para los 6 bloques de colores recientes
        self._column = Column()
        for color in self._recent_colors:
            self._column.add_element(ColoredBlock(block_size, color))
        self._surface = pygame.Surface(self.size, pygame.SRCALPHA)

    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        self._column.set_position(position)
        return self

    def add_color(self, color: tuple[int, int, int]) -> None:
        # Solo agrega el color si no está en _recent_colors
        if color not in self._recent_colors:
            # Insertar el nuevo color al principio y desplazar los demás hacia abajo
            self._recent_colors = [color] + self._recent_colors[:-1]
            # Actualizar los bloques visuales con los colores recientes
            for i, block in enumerate(self._column._elements):
                block.set_color(self._recent_colors[i])

    def get_current_color(self) -> tuple[int, int, int]:
        return self._current_color

    def on_any_event(self, event: Event) -> None:
        if event.type != EventType.MOUSE_BUTTON_DOWN or event.button != MouseButton.LEFT:
            return

        # Detectar si se hace clic en algún bloque de color reciente
        for block in self._column:
            if block.contains(pygame.mouse.get_pos()):
                self._current_color = block.color  # Actualizar el color actual
                break

    def render(self, screen) -> None:
        screen.blit(self._surface, self._position)
        self._column.render(screen)
