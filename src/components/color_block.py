from components.element import Element
import pygame
from events import Event

class ColorBlock(Element):
    _color:tuple[int, int, int] | tuple[int, int, int, int]
    _position: tuple[int, int]
    _surface: pygame.Surface
    def __init__(self,width:int, height:int, color:tuple[int, int, int] | tuple[int, int, int, int]) -> None:
        super().__init__(width, height)
        self._color = color
        self._surface = pygame.Surface((width, height),pygame.SRCALPHA)
        self._surface.fill(self._color)

    def set_position(self, position: tuple[int, int]) -> None:
        self._position = position

    def on_all_events(self, event: Event) -> None:
        pass

    def render(self, screen:pygame.Surface) -> None:
        screen.blit(self._surface,self._position)