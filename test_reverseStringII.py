from unittest import TestCase
from reverse_string_II import Solution
import unittest

class TestSolution(TestCase):
    def test_reverseStringCase1(self):
        sol = Solution()
        self.assertEqual(sol.reverseStr('a',2), 'a')

    def test_reverseStringCase2(self):
        sol = Solution()
        self.assertEqual(sol.reverseStr('abcdefg',2), 'bacdfeg')

    def test_reverseStringCase3(self):
        sol = Solution()
        self.assertEqual(sol.reverseStr('abcdefg',3), 'cbadefg')

    def test_reverseStringCase4(self):
        sol = Solution()
        self.assertEqual(sol.reverseStr('abcdefg',8), 'gfedcba')


if __name__ == '__main__':
    unittest.main()