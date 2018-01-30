from unittest import TestCase
import unittest
from maxsum_subarray import Solution

class TestSolution(TestCase):
    def test_maxsumSubarrayCase1(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_maxsumSubarrayCase2(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1]), 1)

    def test_maxsumSubarrayCase3(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-1]), -1)


if __name__ == '__main__':
    unittest.main()
