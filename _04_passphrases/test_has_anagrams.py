from unittest import TestCase
from _04_passphrases.passphrases import has_anagrams

class TestHasAnagrams(TestCase):

    def test_has_anagrams(self):
        self.assertTrue(has_anagrams(['abc', 'cba', 'xyz']))
        self.assertTrue(has_anagrams(['one', 'two', 'three', 'eno']))
        self.assertFalse(has_anagrams(['one', 'two', 'three']))
        self.assertFalse(has_anagrams(['rxr', 'pom']))
        self.assertTrue(has_anagrams(['rxr', 'pom', 'rxr']))
