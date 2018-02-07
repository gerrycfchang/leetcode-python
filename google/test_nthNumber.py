from unittest import TestCase
import unittest
from nth_number import Solution

class TestSolution(TestCase):
    def test_nthNumberCase1(self):
        sol = Solution()
        self.assertEqual(sol.findNthDigit(13), 1)

    def test_nthNumberCase2(self):
        sol = Solution()
        self.assertEqual(sol.findNthDigit(3), 3)




if __name__ == '__main__':
    unittest.main()