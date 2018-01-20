"""
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the
value 1 in square 1. Then, in the same allocation order as shown above, they store
the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 368078.
"""

from numpy import sign
import math
from typing import Callable


"""
65  64  63  62  61  60  59  58  57
66  37  36  35  34  33  32  31  56
67  38  17  16  15  14  13  30  55
68  39  18   5   4   3  12  29  54
69  40  19   6   1   2  11  28  53
70  41  20   7   8   9  10  27  52
71  42  21  22  23  24  25  26  51
72  43  44  45  46  47  48  49  50
73  74  75  76  77  78  79  80  81
"""


class Grid:

    def __init__(self) -> None:
        self._grid = {}

    def _get_x(self, x: int):
        if not x in self._grid:
            self._grid[x] = {}
        return self._grid[x]

    def get(self, x: int, y: int) -> int:
        grid_x = self._get_x(x)
        if y in grid_x:
            return grid_x[y]
        else:
            return 0

    def set(self, x: int, y: int, value: int) -> None:
        grid_x = self._get_x(x)
        grid_x[y] = value

    def sum_adjacent(self, x: int, y: int) -> int:
        result = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not dx == dy == 0:
                    result += self.get(x + dx, y + dy)
        return result

    def __str__(self) -> str:
        string = ""
        height = len(self._grid[0])
        width = len(self._grid)
        for y in range(- math.ceil(height / 2), math.ceil(height / 2) + 1):
            for x in range(- math.ceil(width / 2), math.ceil(width / 2) + 1):
                string += '{:10d} '.format(self.get(x, -y))
            string += '\n'
        return string


def increment_and_reverse(n: int) -> int:
    return -(n + sign(n))


def build_spiral(grid: Grid,
                 value_function: Callable[[Grid, int, int, int], int],
                 result_function: Callable[[int], int]) -> int:
    x = y = 0
    dx = dy = 1
    result = 0
    value = 1

    grid.set(x, y, value)
    while not result:
        x += sign(dx)
        for x in range(x, x + dx, sign(dx)):
            value = value_function(grid, x, y, value)
            grid.set(x, y, value)
            if not result:
                result = result_function(value)
                if result:
                    return result
        y += sign(dy)
        for y in range(y, y + dy, sign(dy)):
            value = value_function(grid, x, y, value)
            grid.set(x, y, value)
            if not result:
                result = result_function(value)
                if result:
                    return result
        dx = increment_and_reverse(dx)
        dy = increment_and_reverse(dy)

    return result


if __name__ == '__main__':
    input = 368078

    def fn_value(grid: Grid, x: int, y: int, value: int) -> int:
        return grid.sum_adjacent(x, y)

    def fn_found(value: int) -> int:
        return value if value > input else 0

    grid = Grid()
    result = build_spiral(grid, fn_value, fn_found)

    print(grid)
    print(result)
