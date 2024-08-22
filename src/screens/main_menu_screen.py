import pygame

from components import Column, Container, Text, Row, row
from engine import Engine
from events import Event, EventType, KeyEvent, QuitEvent, MouseButton
from screens.screen import Screen


class MainMenuScreen(Screen):
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine
        self.height = engine.get_window_size()[1]
        self.width = engine.get_window_size()[0]

        self.base = Container((self.width, self.height))
        self.base.alignment("center")
        self.base.set_border((0, 132, 134))
        self.base.set_color((0, 132, 134))

        # OPCIONES DE MENU
        column1 = Column()
        column2 = Column()

        title = Container((self.width * 0.3, self.height * 0.2))
        text = Text("NANOGRAM", pygame.font.SysFont("Arial", 50), (99, 99, 224))
        text.set_color((152, 99, 224))
        title.set_child(text)
        title.set_border((255, 255, 255))
        title.set_color((207, 224, 99))
        column1.add_child(title)

        self.button1 = Container((self.width * 0.3, self.height * 0.1))
        self.button1.set_color((207, 178, 171))
        self.button1.set_border((0, 0, 0))
        self.button1.set_child(Text("PLAY", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        column2.add_child(self.button1)

        self.button2 = Container((self.width * 0.3, self.height * 0.1))
        self.button2.set_color((207, 224, 99))
        self.button2.set_border((0, 0, 0))
        self.button2.set_child(Text("CREATE PUZZLE", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        column2.add_child(self.button2)

        self.button3 = Container((self.width * 0.3, self.height * 0.1))
        self.button3.set_color((224, 99, 159))
        self.button3.set_border((0, 0, 0))
        self.button3.set_child(Text("SETTINGS", pygame.font.SysFont("Arial", 30), (0, 0, 0)))
        column2.add_child(self.button3)

        column1.add_child(column2)

        column1.set_separation(self.height * 0.2)
        column2.set_separation(self.height * 0.03)


        # CONTAINERS Y ROWS QUE DIVIDEN EL MENU PRINCIPAL
        container1 = Container((self.width * 0.3, self.height))
        container1.set_border((0, 132, 134))
        container1.set_color((0, 132, 134))
        container1.set_child(column1)

        container2 = Container((self.width * 0.5, self.height))
        container2.set_border((0, 132, 134))
        container2.set_color((0, 132, 134))

        self.row1 = Row()
        self.row1.add_child(container1)
        self.row1.add_child(container2)
        self.row1.set_separation(self.width * 0.03)

        self.base.set_child(self.row1)


    def on_event(self, event: Event) -> None:
        if event.type == EventType.MOUSE_BUTTON_DOWN and event.button == MouseButton.LEFT:
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
        self.base.render(window)
