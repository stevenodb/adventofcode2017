from unittest import TestCase

from _03_spiral_memory import spiral_memory

class TestManhattan(TestCase):
    def test_manhattan(self):
        self.assertEqual(0, spiral_memory.manhattan(1))
        self.assertEqual(1, spiral_memory.manhattan(2))
        self.assertEqual(3, spiral_memory.manhattan(16))
        self.assertEqual(5, spiral_memory.manhattan(48))
        self.assertEqual(6, spiral_memory.manhattan(49))
        self.assertEqual(6, spiral_memory.manhattan(79))
        self.assertEqual(8, spiral_memory.manhattan(73))