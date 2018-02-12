from unittest import TestCase
import unittest
from longest_consecutive_seq import Solution

class TestSolution(TestCase):
    def test_longestConsecutiveSeqCase1(self):
        sol = Solution()
        nums = [100, 4, 200, 1, 3, 2]

        self.assertEqual(sol.longestConsecutive(nums), 4)

if __name__ == '__main__':
    unittest.main()
