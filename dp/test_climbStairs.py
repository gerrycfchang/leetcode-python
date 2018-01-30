from unittest import TestCase
import unittest
from climb_stairs import Solution

class TestSolution(TestCase):
    def test_climbStairsCase1(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(2), 2)

    def test_climbStairsCase2(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(3), 3)

    def test_climbStairsCase3(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(4), 5)


if __name__ == '__main__':
    unittest.main()