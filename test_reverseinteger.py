from unittest import TestCase
from reverse_integer import Solution
import unittest

class TestSolution(TestCase):
    def test_romanToInt(self):
        sol = Solution()
        self.assertEqual(sol.reverse(120), 21)
        self.assertEqual(sol.reverse(-120), -21)
        self.assertEqual(sol.reverse(0), 0)
        self.assertEqual(sol.reverse(-123), -321)
        self.assertEqual(sol.reverse(1534236469), 0)
        self.assertEqual(sol.reverse(900000), 9)
        self.assertEqual(sol.reverse(1563847412), 0)
        self.assertEqual(sol.reverse(-1563847412), 0)

if __name__ == '__main__':
    unittest.main()
