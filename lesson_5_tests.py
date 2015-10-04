import unittest
from lesson_5 import *


class TestCases(unittest.TestCase):
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences('noodle', 'o'), 2)
        self.assertEqual(count_occurrences('alabama', 'a'), 4)
        self.assertEqual(count_occurrences([1, 2, 3, 4, 3, 2, 1], 3), 2)

    def test_find_most_common_item(self):
        self.assertEqual(find_most_common_item('alabama'), 'a')
        self.assertEqual(find_most_common_item([1, 2, 3, 1, 2, 1]), '1')
        self.assertEqual(find_most_common_item('abcab'), 'a')

    def test_find_item_that_occurs_once(self):
        self.assertEqual(find_first_item_that_occurs_once('aabbc'), 'c')
        self.assertEqual(
            find_first_item_that_occurs_once([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(find_first_item_that_occurs_once('abracadabra'), 'c')

    def test_is_anagram(self):
        self.assertEqual(is_anagram('silent', 'listen'), True)
        self.assertEqual(is_anagram('foobar', 'foofoo'), False)

    def test_word_with_only_letters(self):
        self.assertEqual(word_with_only_letters('apple', 'pl'), '_ppl_')

    def test_all_letters_in_word(self):
        self.assertEqual(all_letters_in_word('apple', 'aelp'), True)
        self.assertEqual(all_letters_in_word('apple', 'elpj'), False)


if __name__ == '__main__':
    unittest.main()
