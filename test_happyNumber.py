from unittest import TestCase
import unittest
from happy_number import Solution

class TestSolution(TestCase):
    def test_happyNumberCase1(self):
        sol = Solution()

        self.assertEqual(sol.isHappy(19), True)

if __name__ == '__main__':
    unittest.main()