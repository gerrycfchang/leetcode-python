from unittest import TestCase
import unittest
from move_zeros import Solution

class TestSolution(TestCase):
    def test_moveZerosCase1(self):
        sol = Solution()

        nums = [0, 1, 4, 13, 0]
        exps = [1, 4, 13, 0, 0]
        sol.moveZeroes(nums)

        self.assertListEqual(nums, exps)

if __name__ == '__main__':
    unittest.main()