# src/components/area.py

class Area:
    def __init__(self, dimensions: tuple[int, int]):
        self.width, self.height = dimensions

    def center(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = (self.width - obj_width) // 2
        y = (self.height - obj_height) // 2
        return x, y

    def top_center(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = (self.width - obj_width) // 2
        y = 0
        return x, y

    def bottom_center(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = (self.width - obj_width) // 2
        y = self.height - obj_height
        return x, y

    def top_right(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = self.width - obj_width
        y = 0
        return x, y

    def bottom_right(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = self.width - obj_width
        y = self.height - obj_height
        return x, y

    def top_left(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = 0
        y = 0
        return x, y

    def bottom_left(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = 0
        y = self.height - obj_height
        return x, y

    def center_right(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = self.width - obj_width
        y = (self.height - obj_height) // 2
        return x, y

    def center_left(self, obj_size: tuple[int, int]) -> tuple[int, int]:
        obj_width, obj_height = obj_size
        x = 0
        y = (self.height - obj_height) // 2
        return x, y
