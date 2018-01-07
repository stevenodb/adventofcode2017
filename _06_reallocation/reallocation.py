"""
A debugger program here is having an issue: it is trying to repair a
memory reallocation routine, but it keeps getting stuck in an infinite
loop.

In this area, there are sixteen memory banks; each memory bank can hold
any number of blocks. The goal of the reallocation routine is to balance
the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the
memory bank with the most blocks (ties won by the lowest-numbered memory
bank) and redistributes those blocks among the banks. To do this, it removes
all of the blocks from the selected bank, then moves to the next (by index)
memory bank and inserts one of the blocks. It continues doing this until it
runs out of blocks; if it reaches the last memory bank, it wraps around to
the first one.

The debugger would like to know how many redistributions can be done before
a blocks-in-banks configuration is produced that has been seen before.
"""


def reallocate(cols):

    def hash(cols):
        result = 0
        b = pow(10, len(cols)-1)
        for value in cols:
            result += int(value * b)
            b /= 10
        return result

    def max_index(lst):
        return lst.index(max(lst))

    def cycle(cols):
        idx = max_index(cols)
        block_amount, cols[idx] = cols[idx], 0
        for _ in range(block_amount):
            idx = (idx + 1) % len(cols)
            cols[idx] += 1

    seen = set()
    cycle_count = 0
    while hash(cols) not in seen:
        seen.add(hash(cols))
        cycle(cols)
        cycle_count += 1

    return cycle_count


if __name__ == '__main__':
    with open('input') as file:
        line = file.readline()
    cols = [int(value) for value in line.split()]

    print('Number of cycles: {:d}'.format(reallocate(cols)))
    print('Size of loop from first seen state ({:s}): {:d}'.format(str(cols),reallocate(cols)))
