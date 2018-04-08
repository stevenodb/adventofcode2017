from unittest import TestCase

from _10_knothash.knothash import *


class TestKnotHash(TestCase):

    def test_knot_hash(self):
        (actual, _, _) = knot_hash([3, 4, 1, 5], marks=[x for x in range(5)])
        self.assertEqual(actual, [3, 4, 2, 1, 0])

    def test_reverse_circular_start_at_0_and_no_overflow(self):
        actual = [0, 1, 2, 3, 4]
        reverse_circular(actual, 0, 3)
        self.assertEqual([2, 1, 0, 3, 4], actual)

    def test_reverse_circular_start_at_1_and_no_overflow(self):
        actual = [0, 1, 2, 3, 4]
        reverse_circular(actual, 1, 3)
        self.assertEqual([0, 2, 1, 3, 4], actual)

    def test_reverse_circular_start_at_1_until_end_and_no_overflow(self):
        actual = [0, 1, 2, 3, 4]
        reverse_circular(actual, 1, 5)
        self.assertEqual([0, 4, 3, 2, 1], actual)

    def test_reverse_circular_and_no_overflow(self):
        actual = [0, 1, 2, 3, 4]
        reverse_circular(actual, 0, 5)
        self.assertEqual([4, 3, 2, 1, 0], actual)

    def test_reverse_circular_and_with_overflow(self):
        actual = [0, 1, 2, 3, 4]
        reverse_circular(actual, 4, 2)
        self.assertEqual([0, 4, 2, 3, 1], actual)

    def test_dense_hash_of_empty_string(self):
        actual = dense_knot_hash([])
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', actual)

    def test_dense_hash_of_string_a(self):
        actual = dense_knot_hash(list(map(ord, '1,2,3')))
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', actual)

    def test_dense_hash_of_string_b(self):
        actual = dense_knot_hash(list(map(ord, 'AoC 2017')))
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', actual)
