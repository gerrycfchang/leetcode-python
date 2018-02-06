from unittest import TestCase
import unittest
from palindrome_permutation import Solution

class TestSolution(TestCase):
    def test_palindromePermutationCase1(self):
        sol = Solution()
        self.assertEqual(sol.canPermutePalindrome('code'), False)

    def test_palindromePermutationCase2(self):
        sol = Solution()
        self.assertEqual(sol.canPermutePalindrome('aab'), True)

    def test_palindromePermutationCase3(self):
        sol = Solution()
        self.assertEqual(sol.canPermutePalindrome('carerac'), True)

if __name__ == '__main__':
    unittest.main()