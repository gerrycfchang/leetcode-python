from unittest import TestCase
import unittest
from valid_polindrome_II import Solution

class TestSolution(TestCase):
    def test_validPalindromeIICase1(self):
        sol = Solution()

        self.assertEqual(sol.validPalindrome("aba"),True)

    def test_validPalindromeIICase2(self):
        sol = Solution()
        self.assertEqual(sol.validPalindrome("abca"), True)


if __name__ == '__main__':
    unittest.main()