from unittest import TestCase
from _07_recursive_circus.circus import parse_entry, PATTERN


class TestParseEntry(TestCase):

    """
    polkn (91947) -> dvqaks, fnubw, xlhbak
    xmufd (16)
    mtrumh (81)
    vebkntv (87) -> qdyxf, xqkov
    ffqzxf (17)
    mstjkgi (178) -> jyppp, oyatv, hpvsz
    """
    def test_parse_entry_with_tail(self):
        dict = parse_entry('tjiqr (87) -> avcwghu, cfqpega, ipbtx, fpmomi', PATTERN)
        self.assertEqual(dict['name'], 'tjiqr')
        self.assertEqual(int(dict['weight']), 87)
        self.assertEqual(dict['children'], 'avcwghu, cfqpega, ipbtx, fpmomi')


    def test_parse_entry_without_tail(self):
        dict = parse_entry('tjiqr (87)', PATTERN)
        self.assertEqual(dict['name'], 'tjiqr')
        self.assertEqual(int(dict['weight']), 87)
        self.assertIsNone(dict['children'])
