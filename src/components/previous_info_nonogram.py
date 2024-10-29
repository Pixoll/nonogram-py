from components import Element
from core.nonogram import Nonogram
from components import Text
import pygame
class PreviousInfoNonogram(Element):
    _nonogram: Nonogram
    _size: Text
    def __init__(self, nonogram: Nonogram, ) ->None:
        super().__init__(nonogram.size[0]*25,nonogram.size[1]*25 )
        self.nonogram = nonogram
        size = f"{nonogram.size[0]}x{nonogram.size[1]}"
        self._size = Text(size,pygame.font.SysFont("Arial",60),(99, 99, 224)).set_position((self.size[0],self.size[1]//4))




