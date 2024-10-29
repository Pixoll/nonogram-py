from typing import Self
from unittest import TestCase

from pygame import Surface

from components.element import Element
from events import Event


class ElementImpl(Element):
    def set_position(self, position: tuple[int, int]) -> Self:
        self._position = position
        return self

    def on_any_event(self, event: Event) -> None:
        pass

    def render(self, window: Surface) -> None:
        pass


class TestElement(TestCase):
    def setUp(self):
        self.element = ElementImpl(50, 100)

    def test_initial_size(self):
        self.assertEqual(self.element.size, (50, 100))

    def test_initial_position(self):
        self.assertEqual(self.element.position, (0, 0))

    def test_set_position(self):
        self.element.set_position((10, 20))
        self.assertEqual(self.element.position, (10, 20))

    def test_contains_inside(self):
        self.element.set_position((10, 20))
        self.assertTrue(self.element.contains((30, 50)))

    def test_contains_outside(self):
        self.element.set_position((10, 20))
        self.assertFalse(self.element.contains((70, 150)))

    def test_contains_corners(self):
        self.element.set_position((10, 20))
        self.assertTrue(self.element.contains((10, 20)))
        self.assertTrue(self.element.contains((60, 120)))
