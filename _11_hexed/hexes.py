"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to
you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north,
northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the
fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any
adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""

from typing import Dict, Callable, Tuple

DIRECTIONS: Dict[str, Callable[[int, int, int], Tuple[int, int, int]]] = \
    {
        'n': lambda x, y, z: (x, y + 1, z - 1),
        'ne': lambda x, y, z: (x + 1, y, z - 1),
        'se': lambda x, y, z: (x + 1, y - 1, z),
        's': lambda x, y, z: (x, y - 1, z + 1),
        'sw': lambda x, y, z: (x - 1, y, z + 1),
        'nw': lambda x, y, z: (x - 1, y + 1, z)
    }

with open('input') as f:
    line = f.read()
    directions = line.split(',')

    x = 0
    y = 0
    z = 0
    max_dist = 0

    for direction in directions:
        f = DIRECTIONS[direction]
        (x, y, z) = f(x, y, z)
        distance = (abs(x) + abs(y) + abs(z)) / 2
        max_dist = max(distance, max_dist)

    distance = (abs(x) + abs(y) + abs(z)) / 2
    print('x:' + str(x), 'y:' + str(y), 'z:' + str(z))
    print('distance: ' + str(distance))
    print('max distance: ' + str(max_dist))

    # x:406 + 2 / y:136 = 3 => 406 / (1/2) = 812
