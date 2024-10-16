from os.path import exists
from shutil import rmtree
from unittest import TestCase

from core.nonogram import Nonogram


class TestNonogram(TestCase):
    def setUp(self):
        self.nonogram_data = [
            [(0, 0, 0), (255, 255, 255), (255, 0, 0)],
            [None, (255, 255, 255), (0, 0, 255)]
        ]

        self.nonogram = Nonogram(self.nonogram_data, "custom")

    def tearDown(self):
        if exists("nonograms"):
            rmtree("nonograms")

    def test_initialization(self):
        self.assertEqual(self.nonogram.size, (3, 2))
        self.assertEqual(sorted(self.nonogram.used_colors), sorted(((0, 0, 0), (255, 0, 0), (0, 0, 255))))

    def test_horizontal_hints(self):
        self.assertEqual(self.nonogram.horizontal_hints[0][0].value, 1)
        self.assertEqual(self.nonogram.horizontal_hints[1][0].value, 1)

    def test_vertical_hints(self):
        self.assertEqual(self.nonogram.vertical_hints[0][0].value, 1)
        self.assertEqual(self.nonogram.vertical_hints[2][0].value, 1)

    def test_completion(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[1, 0] = None
        self.nonogram[2, 0] = (255, 0, 0)
        self.nonogram[0, 1] = None
        self.nonogram[1, 1] = None
        self.nonogram[2, 1] = (0, 0, 255)
        self.assertTrue(self.nonogram.is_completed)

    def test_save_load(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram.save()
        loaded_nonogram = Nonogram.load("custom", 1)
        self.assertEqual(self.nonogram.size, loaded_nonogram.size)
        self.assertEqual(self.nonogram.used_colors, loaded_nonogram.used_colors)
        self.assertEqual(
            [[(h.value, h.color) for h in hint] for hint in self.nonogram.horizontal_hints],
            [[(h.value, h.color) for h in hint] for hint in loaded_nonogram.horizontal_hints]
        )
        self.assertEqual(
            [[(h.value, h.color) for h in hint] for hint in self.nonogram.vertical_hints],
            [[(h.value, h.color) for h in hint] for hint in loaded_nonogram.vertical_hints]
        )
        self.assertEqual(self.nonogram._original, loaded_nonogram._original)
        self.assertEqual(self.nonogram._player_grid, loaded_nonogram._player_grid)
        self.assertEqual(self.nonogram._palette, loaded_nonogram._palette)

    def test_is_row_complete(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[1, 0] = None
        self.nonogram[2, 0] = (255, 0, 0)
        self.assertTrue(self.nonogram.is_row_complete(0))

    def test_is_column_complete(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[0, 1] = None
        self.assertTrue(self.nonogram.is_column_complete(0))
