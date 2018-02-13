from unittest import TestCase
import unittest
from combination_sum_IV import Solution

class TestSolution(TestCase):
    def test_combinationSumIVCase1(self):
        sol = Solution()
        nums = [1,2,3]
        self.assertEqual(sol.combinationSum4(nums, 4), 7)

    
if __name__ == '__main__':
    unittest.main()