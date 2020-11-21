import unittest
from BagsTracker import find_min_size


class BagsTracker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_min_size(1, 1, 100), 100)

    def test_2(self):
        self.assertEqual(find_min_size(14, 3459809345, 34534589), 3459809345)

    def test_3(self):
        self.assertEqual(find_min_size(10, 10, 1), 10)

    def test_4(self):
        self.assertEqual(find_min_size(10, 2, 3), 9)

