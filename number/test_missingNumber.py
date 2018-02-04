from unittest import TestCase
from missing_number import Solution
import unittest

class TestSolution(TestCase):
    def test_missingNumberCase1(self):
        sol = Solution()

        self.assertEqual(sol.missingNumber([3,0,1]), 2)

if __name__ == '__main__':
    unittest.main()