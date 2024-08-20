import pygame

from components import Column, Container, Text
from engine import Engine
from screens.screen import Screen
from events import Event, QuitEvent, KeyEvent


class MenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

        self.menu = Container((1280, 720))
        self.menu.alignment("center")

        title1 = Container((200, 100))
        text = Text("NANOGRAM", pygame.font.SysFont("Arial", 30), (99, 99, 224))
        text.set_color((152, 99, 224))
        title1.set_child(text)
        title1.set_border((255, 255, 255))

        button1 = Container((200, 100))
        button1.set_color((207, 178, 171))
        button1.set_border((0, 0, 0))
        button1.set_child(Text("PLAY", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        button2 = Container((200, 100))
        button2.set_color((207, 224, 99))
        button2.set_border((0, 0, 0))
        button2.set_child(Text("CREATE PUZZLE", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        button3 = Container((200, 100))
        button3.set_color((224, 99, 159))
        button3.set_border((0, 0, 0))
        button3.set_child(Text("SETTINGS", pygame.font.SysFont("Arial", 30), (0, 0, 0)))

        column = Column()
        column.add_child(title1)
        column.add_child(Container((25, 50)))
        column.add_child(button1)
        column.add_child(Container((25, 25)))
        column.add_child(button2)
        column.add_child(Container((25, 25)))
        column.add_child(button3)

        self.menu.set_child(column)

        self.button1 = button1
        self.button2 = button2
        self.button3 = button3

    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.button1.position[0] <= mouse_pos[0] <= self.button1.position[0] + self.button1.width and \
                    self.button1.position[1] <= mouse_pos[1] <= self.button1.position[1] + self.button1.height:
                from screens.play_screen import PlayScreen
                self.engine.set_screen(PlayScreen(self.engine))

            elif self.button2.position[0] <= mouse_pos[0] <= self.button2.position[0] + self.button2.width and \
                    self.button2.position[1] <= mouse_pos[1] <= self.button2.position[1] + self.button2.height:
                from screens.create_screen import CreateScreen
                self.engine.set_screen(CreateScreen(self.engine))

            elif self.button3.position[0] <= mouse_pos[0] <= self.button3.position[0] + self.button3.width and \
                    self.button3.position[1] <= mouse_pos[1] <= self.button3.position[1] + self.button3.height:
                from screens.settings_screen import SettingsScreen
                self.engine.set_screen(SettingsScreen(self.engine))

    def on_key_event(self, key_event: KeyEvent) -> None:
        pass

    def on_quit_event(self, key_event: QuitEvent) -> None:
        pass

    def render(self) -> None:
        window = pygame.display.get_surface()
        self.menu.render(window)
