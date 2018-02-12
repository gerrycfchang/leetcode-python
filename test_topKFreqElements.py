from unittest import TestCase
import unittest
from top_k_freq_elements import Solution


class TestSolution(TestCase):
    def test_topKFreqElementsCase1(self):
        sol = Solution()
        nums = [1,1,1,2,2,3]

        self.assertListEqual(sol.topKFrequent(nums, 2),[2,1])

if __name__ == '__main__':
    unittest.main()