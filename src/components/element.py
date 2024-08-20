from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def render(self, window):
        pass

    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def set_position(self, position: tuple[int, int]):
        pass
