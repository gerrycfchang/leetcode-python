from unittest import TestCase
import unittest
from combination_sum_III import Solution

class TestSolution(TestCase):
    def test_combinationSumIIICase1(self):
        sol = Solution()
        exp = [[1,2,4]]
        self.assertListEqual(sol.combinationSumIII(3, 7), exp)

    def test_combinationSumIIICase2(self):
        sol = Solution()
        exp = [[1,2,6], [1,3,5], [2,3,4]]
        self.assertListEqual(sol.combinationSumIII(3, 9), exp)

    def test_combinationSumIIICase3(self):
        sol = Solution()
        exp = []
        self.assertListEqual(sol.combinationSumIII(2, 18), exp)
    
    def test_combinationSumIIICase4(self):
        sol = Solution()
        exp = [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
        self.assertListEqual(sol.combinationSumIII(3, 15), exp)

    
if __name__ == '__main__':
    unittest.main()