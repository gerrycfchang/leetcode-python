from unittest import TestCase
import unittest
from reverse_vowels_of_string import Solution

class TestSolution(TestCase):
    def test_reverseStringsCase1(self):
        sol = Solution()
        self.assertEqual(sol.reverseVowels('hello'),'holle')

    def test_reverseStringsCase2(self):
        sol = Solution()
        self.assertEqual(sol.reverseVowels('aA'), 'Aa')



if __name__ == '__main__':
    unittest.main()