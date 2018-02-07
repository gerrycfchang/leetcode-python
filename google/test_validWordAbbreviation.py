from unittest import TestCase
import unittest
from valid_word_abbreviation import Solution

class TestSolution(TestCase):
    def test_validWordAbbrCase1(self):
        sol = Solution()

        self.assertEqual(sol.validWordAbbreviation('word','w2d'), True)
        self.assertEqual(sol.validWordAbbreviation('word', '3d'), True)
        self.assertEqual(sol.validWordAbbreviation('word', '10d'), False)
        self.assertEqual(sol.validWordAbbreviation('word', 'w1xd'), False)


if __name__ == '__main__':
    unittest.main()