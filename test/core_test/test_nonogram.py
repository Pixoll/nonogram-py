from os.path import exists
from shutil import rmtree
from unittest import TestCase

from core import Nonogram


class TestNonogram(TestCase):
    def setUp(self):
        self.nonogram_data = [
            [(0, 0, 0), (255, 255, 255), (255, 0, 0)],
            [None, (255, 255, 255), (0, 0, 255)]
        ]

        self.nonogram = Nonogram(self.nonogram_data, "pre_made", nonogram_name="My nonogram")

    def tearDown(self):
        if exists("nonograms"):
            rmtree("nonograms")

    def test_initialization(self):
        self.assertEqual(self.nonogram.size, (3, 2))
        self.assertEqual(sorted(self.nonogram.used_colors), sorted(((0, 0, 0), (255, 0, 0), (0, 0, 255))))

    def test_nonogram_name(self):
        self.assertEqual(self.nonogram.name, "My nonogram")

    def test_horizontal_hints(self):
        self.assertEqual(self.nonogram.horizontal_hints[0][0].value, 1)
        self.assertEqual(self.nonogram.horizontal_hints[1][0].value, 1)

    def test_vertical_hints(self):
        self.assertEqual(self.nonogram.vertical_hints[0][0].value, 1)
        self.assertEqual(self.nonogram.vertical_hints[2][0].value, 1)

    def test_completion(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[1, 0] = "x"
        self.nonogram[2, 0] = (255, 0, 0)
        self.nonogram[0, 1] = "x"
        self.nonogram[1, 1] = "x"
        self.nonogram[2, 1] = (0, 0, 255)
        self.assertTrue(self.nonogram.is_completed)

    def test_is_row_complete(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[1, 0] = "x"
        self.nonogram[2, 0] = (255, 0, 0)
        self.assertTrue(self.nonogram.is_row_complete(0))

    def test_is_column_complete(self):
        self.nonogram[0, 0] = (0, 0, 0)
        self.nonogram[0, 1] = "x"
        self.assertTrue(self.nonogram.is_column_complete(0))
