from unittest import TestCase
from _02_corruption_checksum import integer_division


class TestPossible_division(TestCase):
    def test_possible_division(self):
        self.assertEqual(4, integer_division.possible_division([2, 3, 7, 8]))
        self.assertEqual(4, integer_division.possible_division([8, 3, 7, 2]))
