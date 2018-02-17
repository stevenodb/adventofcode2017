from unittest import TestCase
from _09_streams.stream_processing import *


class TestStreamProcessing(TestCase):

    """
    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.
    {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    {<a>,<a>,<a>,<a>}, score of 1.
    {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
    """
    def test_process_score(self):
        self.assertEqual(1, process('{}').get('score'))
        self.assertEqual(6, process('{{{}}}').get('score'))
        self.assertEqual(5, process('{{},{}}').get('score'))
        self.assertEqual(16, process('{{{},{},{{}}}}').get('score'))
        self.assertEqual(1, process('{<a>,<a>,<a>,<a>}').get('score'))
        self.assertEqual(9, process('{{<ab>},{<ab>},{<ab>},{<ab>}}').get('score'))
        self.assertEqual(9, process('{{<!!>},{<!!>},{<!!>},{<!!>}}').get('score'))
        self.assertEqual(3, process('{{<a!>},{<a!>},{<a!>},{<ab>}}').get('score'))

    """
    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.
    """
    def test_process_n_garbage(self):
        self.assertEqual(0, process("<>").get('n_garbage'))
        self.assertEqual(17, process("<random characters>").get('n_garbage'))
        self.assertEqual(3, process("<<<<>").get('n_garbage'))
        self.assertEqual(2, process("<{!>}>").get('n_garbage'))
        self.assertEqual(0, process("<!!>").get('n_garbage'))
        self.assertEqual(0, process("<!!!>>").get('n_garbage'))
        self.assertEqual(10, process("<{o\"i!a,<{i<a>").get('n_garbage'))
