import unittest
from BagsTracker import get_min_size_of_square


class BagsTracker(unittest.TestCase):
    def test_one_element(self):
        self.assertEqual(get_min_size_of_square(1, 1, 100), 100)
        self.assertEqual(get_min_size_of_square(1, 100, 1), 100)

    def test_big_numbers(self):
        self.assertEqual(get_min_size_of_square(10, 100000000, 99999999), 399999996)

    def test_width_is_one(self):
        self.assertEqual(get_min_size_of_square(10, 1, 10), 10)

    def test_height_is_one(self):
        self.assertEqual(get_min_size_of_square(10, 10, 1), 10)

    def test_from_condition(self):
        self.assertEqual(get_min_size_of_square(10, 2, 3), 9)
