from unittest import TestCase
import unittest
from combination_sum_IV import Solution

class TestSolution(TestCase):
    def test_combinationSumIVCase1(self):
        sol = Solution()
        nums = [1,2,3]
        self.assertEqual(sol.combinationSum4(nums, 4), 7)

    def test_combinationSumIVCase2(self):
        sol = Solution()
        nums = [2, 3, 6, 7]
        self.assertEqual(sol.combinationSum4(nums, 7), 4)

    def test_combinationSumIVCase3(self):
        sol = Solution()
        nums = [3, 1, 2, 4]
        self.assertEqual(sol.combinationSum4(nums, 4), 8)

    def test_combinationSumIVCase4(self):
        sol = Solution()
        nums = [4, 2, 1]
        self.assertEqual(sol.combinationSum4(nums, 32), 39882198)

    
if __name__ == '__main__':
    unittest.main()