from unittest import TestCase
from _03_spiral_memory import spiral_memory_sum


class TestBuild_spiral(TestCase):

    def test_build_spiral(self):
        grid = spiral_memory_sum.Grid()
        spiral_memory_sum.build_spiral(grid, lambda grid, x, y, value: value + 1, lambda result: result >= 42)
        print(grid)
        self.assertEqual(grid.get(0, 0), 1)
        self.assertEqual(grid.get(2, 2), 13)
        self.assertEqual(grid.get(-3, -2), 42)