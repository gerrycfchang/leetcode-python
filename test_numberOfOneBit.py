from unittest import TestCase
import unittest
from number_one_bit import Solution

class TestSolution(TestCase):
    def test_numberOfBitsCase1(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(1), 1)

    def test_numberOfBitsCase2(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(10), 2)


if __name__ == '__main__':
    unittest.main()
