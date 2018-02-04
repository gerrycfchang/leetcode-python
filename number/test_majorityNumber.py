from unittest import TestCase
import unittest
from majority_number import Solution

class TestSolution(TestCase):
    def test_majorityNumberCase1(self):
        sol = Solution()

        self.assertEqual(sol.majorityElement([1, 2, 2, 2, 3]), 2)

if __name__ == '__main__':
    unittest.main()