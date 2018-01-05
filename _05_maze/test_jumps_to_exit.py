from unittest import TestCase
from _05_maze import maze


class TestMaze(TestCase):

    def test_jumps_to_exit(self):
        self.assertEqual(maze.jumps_to_exit([0, 3, 0, 1, -3]), 5)

    def test_jumps_to_exit_part2(self):
        self.assertEqual(maze.jumps_to_exit_part2([0, 3, 0, 1, -3]), 10)
