from unittest import TestCase
from merge_sorted_array import Solution
import unittest

class TestSolution(TestCase):
    def test_mergeCase1(self):
        sol = Solution()
        nums1 = [1, 0]
        nums2 = [2]

        sol.merge(nums1, 1, nums2, 1)
        self.assertListEqual(nums1,[1,2])

    def test_mergeCase2(self):
        sol = Solution()
        nums1 = [0]
        nums2 = [1]

        sol.merge(nums1, 0, nums2, 1)
        self.assertListEqual(nums1,[1])

if __name__ == '__main__':
    unittest.main()