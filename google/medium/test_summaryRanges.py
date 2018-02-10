from unittest import TestCase
import unittest
from summary_ranges import Solution


class TestSolution(TestCase):
    def test_summaryRangesCase1(self):
        sol = Solution()

        nums = [0,1,2,4,5,7]

        exp = ["0->2","4->5","7"]

        self.assertListEqual(sol.summaryRanges(nums), exp)

    def test_summaryRangesCase2(self):
        sol = Solution()

        nums = [0,2,3,4,6,8,9]

        exp = ["0","2->4","6","8->9"]

        self.assertListEqual(sol.summaryRanges(nums), exp)

if __name__ == '__main__':
    unittest.main()
