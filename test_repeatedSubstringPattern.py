from unittest import TestCase
import unittest
from repeated_substring_pattern import Solution


class TestSolution(TestCase):
    def test_repeatedSustringPatternCase1(self):
        sol = Solution()
        self.assertEqual(sol.repeatedSubstringPattern('abab'), True)

    def test_repeatedSustringPatternCase2(self):
        sol = Solution()
        self.assertEqual(sol.repeatedSubstringPattern('bcabca'), True)

    def test_repeatedSustringPatternCase3(self):
        sol = Solution()
        self.assertEqual(sol.repeatedSubstringPattern('abcabcabcabc'), True)

    def test_repeatedSustringPatternCase4(self):
        sol = Solution()
        self.assertEqual(sol.repeatedSubstringPattern('bb'), True)

    def test_repeatedSustringPatternCase5(self):
        sol = Solution()
        self.assertEqual(sol.repeatedSubstringPattern('aabaab'), True)


if __name__ == '__main__':
    unittest.main()