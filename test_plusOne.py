from unittest import TestCase
import unittest

from plus_one import Solution

class TestSolution(TestCase):
    def test_plusOneCase1(self):
        sol = Solution()
        exp = [1]

        self.assertListEqual(sol.plusOne([0]),exp)

    def test_plusOneCase2(self):
        sol = Solution()
        exp = [1,0]

        self.assertListEqual(sol.plusOne([9]),exp)

    def test_plusOneCase3(self):
        sol = Solution()
        exp = [1,0,0]

        self.assertListEqual(sol.plusOne([9,9]),exp)

if __name__ == '__main__':
    unittest.main()