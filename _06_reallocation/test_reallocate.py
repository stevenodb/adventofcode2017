from unittest import TestCase
from _06_reallocation import reallocation


class TestReallocate(TestCase):
    def test_reallocate(self):
        actual = reallocation.reallocate([0, 2, 7, 0])
        self.assertEqual(actual, 5)
