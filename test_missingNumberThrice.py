from unittest import TestCase
from missing_number_thrice import Solution
import unittest

class TestSolution(TestCase):
    def test_missingNumberThriceCase1(self):
        sol = Solution()

        self.assertEqual(sol.findMissingNumber([1, 1, 1, 2, 2, 3, 3, 3]), 2)

    def test_missingNumberThriceCase2(self):
        sol = Solution()

        self.assertEqual(sol.findMissingNumber([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6]), 5)

if __name__ == '__main__':
    unittest.main()