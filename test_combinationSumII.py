from unittest import TestCase
import unittest
from combination_sum_II import Solution

class TestSolution(TestCase):
    def test_combinationSumIICase1(self):
        sol = Solution()
        nums = [10, 1, 2, 7, 6, 1, 5]
        exp = [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
            ]
        self.assertListEqual(sorted(sol.combinationSumII(nums, 8)), sorted(exp))

    
if __name__ == '__main__':
    unittest.main()