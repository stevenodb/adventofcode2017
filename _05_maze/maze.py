"""
Positive jumps ("forward") move downward; negative jumps move upward.
For legibility in this example, these offset values will be written
all on one line, with the current instruction marked in parentheses.
The following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
    Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified.
    The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

In this example, the exit is reached in 5 steps.
"""


def jumps_to_exit(instructions):
    idx = 0
    step_count = 0
    jumps = instructions[:]
    while idx < len(jumps):
        offset = jumps[idx]
        jumps[idx] += 1
        idx = idx + offset
        step_count += 1
    return step_count


def jumps_to_exit_part2(instructions):
    idx = 0
    step_count = 0
    jumps = instructions[:]
    while idx < len(jumps):
        offset = jumps[idx]
        jumps[idx] += -1 if offset > 2 else 1
        idx = idx + offset
        step_count += 1
    return step_count


if __name__ == '__main__':
    # jumps = [0, 3, 0, 1, -3]

    with open('input') as file:
        lines = file.readlines()

    jumps = [int(line) for line in lines]

    print(jumps_to_exit(jumps))
    print(jumps_to_exit_part2(jumps))
