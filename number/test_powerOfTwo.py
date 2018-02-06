from unittest import TestCase
import unittest
from power_of_two import Solution

class TestSolution(TestCase):
    def test_powerOfTwoCase1(self):
        sol = Solution()
        self.assertEqual(sol.isPowerOfTwo(1), True)
        self.assertEqual(sol.isPowerOfTwo(-16), False)

if __name__ == '__main__':
    unittest.main()
