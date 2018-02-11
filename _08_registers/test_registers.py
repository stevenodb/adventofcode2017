from unittest import TestCase

from _08_registers.registers import *

class TestRegisters(TestCase):

    def test_eval_instruction_condition__true_condition_evals_to_True(self):
        instruction = {'register': 'o', 'operation': 'dec', 'amount': '-427', 'condition': 'wnh < -1', 'condition_register': 'wnh'}
        registers = {'wnh': -2}
        actual = eval_condition(instruction, registers)
        self.assertEqual(actual, True)

    def test_eval_instruction_condition__false_condition_evals_to_False(self):
        instruction = {'register': 'o', 'operation': 'dec', 'amount': '-427', 'condition': 'wnh < -1', 'condition_register': 'wnh'}
        registers = {'wnh': 1}
        actual = eval_condition(instruction, registers)
        self.assertEqual(actual, False)

    def test_eval_instruction_condition__condition_register_default_is_0(self):
        instruction = {'register': 'o', 'operation': 'dec', 'amount': '-427', 'condition': 'wnh == 0', 'condition_register': 'wnh'}
        registers = {}
        actual = eval_condition(instruction, registers)
        self.assertEqual(actual, True)

    def test_exec_instruction(self):
        instruction = {'register': 'o', 'operation': 'dec', 'amount': '-427', 'condition': 'wnh < -1', 'condition_register': 'wnh'}
        registers = {'wnh': -2}
        exec_instruction(instruction, registers)
        self.assertEqual(registers['o'], 427)
