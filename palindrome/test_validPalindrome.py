from unittest import TestCase
import unittest
from valid_palindrome import Solution

class TestSolution(TestCase):
    def test_validPalindromeCase1(self):
        sol = Solution()

        self.assertEqual(sol.isPalindrome(""),True)

    def test_validPalindromeCase2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(" "), True)

    def test_validPalindromeCase3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(".a"), True)

    def test_validPalindromeCase4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("ab"), False)

    def test_validPalindromeCase5(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("aA"), True)

if __name__ == '__main__':
    unittest.main()