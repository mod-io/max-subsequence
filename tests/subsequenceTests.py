#!/usr/bin/env python3
import unittest
from subsequence import hvlcs

#Test max subsequence and optimal value
class TestHVLCS(unittest.TestCase):

    def test_empty_both_strings(self):
        charVal = {'a': 2, 'b': 4}
        value, subseq = hvlcs("", "", charVal)
        self.assertEqual(value, 0)
        self.assertEqual(subseq, "")

    def test_empty_string_a(self):
        charVal = {'a': 2, 'b': 4}
        value, subseq = hvlcs("", "ab", charVal)
        self.assertEqual(value, 0)
        self.assertEqual(subseq, "")

    def test_empty_string_b(self):
        charVal = {'a': 2, 'b': 4}
        value, subseq = hvlcs("ab", "", charVal)
        self.assertEqual(value, 0)
        self.assertEqual(subseq, "")

    def test_no_common_characters(self):
        charVal = {'a': 2, 'b': 4, 'c': 5, 'd': 3}
        value, subseq = hvlcs("aaa", "bbb", charVal)
        self.assertEqual(value, 0)
        self.assertEqual(subseq, "")

    def test_identical_strings(self):
        charVal = {'a': 2, 'b': 4, 'c': 5}
        value, subseq = hvlcs("abc", "abc", charVal)
        self.assertEqual(value, 11)   # 2+4+5
        self.assertEqual(subseq, "abc")

    def test_single_char_match(self):
        charVal = {'a': 7, 'b': 3}
        value, subseq = hvlcs("a", "a", charVal)
        self.assertEqual(value, 7)
        self.assertEqual(subseq, "a")

    def test_single_char_no_match(self):
        charVal = {'a': 7, 'b': 3}
        value, subseq = hvlcs("a", "b", charVal)
        self.assertEqual(value, 0)
        self.assertEqual(subseq, "")

if __name__ == "__main__":
    unittest.main()