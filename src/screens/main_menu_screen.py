from pygame.event import Event
import pygame

from src.utils.column import Column
from src.utils.container import Container
from src.utils.text import Text
from src.utils.row import Row
from src.engine import Engine
from src.screens.screen import Screen


class MainMenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

        self.design = Container((1280, 720))
        self.design.set_color((255, 255, 255))
        self.design.alignment("center")

        container1 = Container((200, 100))
        container1.set_color((207, 178, 171))
        container2 = Container((200, 100))
        container2.set_color((207, 224, 99))
        container3 = Container((200, 100))
        container3.set_color((99, 224, 190))
        container4 = Container((200, 100))
        container4.set_color((152, 99, 224))
        container5 = Container((200, 100))
        container5.set_color((152, 224, 190))
        container6 = Container((200, 100))
        container6.set_color((224, 99, 159))
        container7 = Container((200, 100))
        container7.set_color((99, 99, 224))

        texto1 = Text("sus",pygame.font.SysFont('Arial', 30),(99, 99, 224))
        container1.set_child(texto1)
        container2.set_child(texto1)
        container1.alignment("centerLeft")

        row1 = Row()
        row1.add_child(container1)
        row1.add_child(container2)
        row1.add_child(container3)

        column1 = Column()
        column1.add_child(row1)
        column1.add_child(container4)
        column1.add_child(container5)
        column1.add_child(container6)
        column1.add_child(container7)

        self.design.set_child(column1)

    def run_logic(self, event: Event) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.design.render(window)