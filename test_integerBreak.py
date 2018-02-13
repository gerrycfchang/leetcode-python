from unittest import TestCase
import unittest
from integer_break import Solution

class TestSolution(TestCase):
    def test_integerBreakCase1(self):
        sol = Solution()
        self.assertEqual(sol.integerBreak(4), 4)

    def test_integerBreakCase2(self):
        sol = Solution()
        self.assertEqual(sol.integerBreak(3), 2)

    def test_integerBreakCase3(self):
        sol = Solution()
        self.assertEqual(sol.integerBreak(6), 9)

if __name__ == '__main__':
    unittest.main()