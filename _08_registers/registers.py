"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with
jump instructions, it would like you to compute the result of a series of unusual
register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction without
modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5 -> a = 1
c dec -10 if a >= 1 -> a = 1, c = 10
c inc -20 if c == 10 -> a = 1, c = -10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However,
the CPU doesn't have the bandwidth to tell you what all the registers are named, and
leaves that to you to determine.

What is the largest value in any register after completing the instructions in your
puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during
this process so that it can decide how much memory to allocate to these operations.
For example, in the above instructions, the highest value ever held was 10 (in
register c after the third instruction was evaluated).

"""
import re
from typing import Dict, AnyStr

CONDITION_REGISTER = 'condition_register'

REGISTER = 'register'
OPERATION = 'operation'
AMOUNT = 'amount'
CONDITION = 'condition'


def parse_line(line: AnyStr) -> Dict:
    pattern = re.compile(r"^(?P<register>\w*)\s+"
                         r"(?P<operation>inc|dec)\s+"
                         r"(?P<amount>-?\d+)\s+"
                         r"if\s+(?P<condition>(?P<condition_register>\w+).*?)\s*$")
    match_result = pattern.match(line)
    return match_result.groupdict()


def eval_condition(instruction: Dict, registers: Dict) -> bool:
    default_scope = {instruction[CONDITION_REGISTER]: 0}
    return eval(instruction[CONDITION], default_scope, registers)


def exec_instruction(instruction: Dict, registers: Dict) -> None:
    operation = {
        'inc': lambda val, amount: val + amount,
        'dec': lambda val, amount: val - amount
    }[instruction[OPERATION]]

    variable = instruction[REGISTER]

    value = registers[variable] if variable in registers else 0
    amount = int(instruction[AMOUNT])

    registers[variable] = operation(value, amount)


if __name__ == '__main__':
    registers = {}
    highest_register = 0

    with open('input') as f:
        for line in f:
            instruction = parse_line(line)
            if eval_condition(instruction, registers):
                exec_instruction(instruction, registers)
                highest_register = max(max(registers.values()), highest_register)
    print('Max value in final register configuration: %i' % max(registers.values()))
    print('Highest register overall: %i' % highest_register)