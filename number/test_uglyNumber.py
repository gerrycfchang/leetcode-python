from unittest import TestCase
import unittest
from ugly_number import Solution

class TestSolution(TestCase):
    def test_uglyNumberCase1(self):
        sol = Solution()

        self.assertEqual(sol.isUgly(8), True)

    def test_uglyNumberCase2(self):
        sol = Solution()

        self.assertEqual(sol.isUgly(7), False)

    def test_uglyNumberCase3(self):
        sol = Solution()

        self.assertEqual(sol.isUgly(40), True)


if __name__ == '__main__':
    unittest.main()