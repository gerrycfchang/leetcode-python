from unittest import TestCase
import unittest
from combination_sum import Solution

class TestSolution(TestCase):
    def test_combinationSumIVCase1(self):
        sol = Solution()
        nums = [2,3,6,7]
        exp = [[2,2,3],[7]]
        self.assertListEqual(sol.combinationSum(nums, 7), exp)

    
if __name__ == '__main__':
    unittest.main()