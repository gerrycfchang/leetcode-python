from unittest import TestCase
import unittest
from majority_number_II import Solution

class TestSolution(TestCase):
    def test_majorityNumberIICase1(self):
        sol = Solution()

        self.assertListEqual(sol.majorityElement([]), [])

    def test_majorityNumberIICase2(self):
        sol = Solution()

        result = sol.majorityElement([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9])
        result.sort()
        self.assertListEqual(result, [3,9])

    def test_majorityNumberIICase3(self):
        sol = Solution()

        result = sol.majorityElement([1, 2, 1, 2, 1, 3, 3])
        result.sort()
        self.assertListEqual(result, [1])

if __name__ == '__main__':
    unittest.main()