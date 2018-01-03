from unittest import TestCase
from _04_passphrases.passphrases import has_duplicates


class TestHas_duplicates(TestCase):
    def test_has_duplicates(self):
        self.assertTrue(has_duplicates(['one','two','three','one']))
        self.assertTrue(has_duplicates(['one', 'two', '', '']))
        self.assertTrue(has_duplicates(['one', 'two', 'one', 'one']))
        self.assertFalse(has_duplicates(['one', 'two', 'three', 'four']))
