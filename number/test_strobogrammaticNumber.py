from unittest import TestCase
import unittest
from strobogrammatic_number import Solution


class TestSolution(TestCase):
    def test_strobogrammaticNumberCase1(self):
        sol = Solution()

        self.assertEqual(sol.isStrobogrammatic(13), False)
        self.assertEqual(sol.isStrobogrammatic(16791), False)

        self.assertEqual(sol.isStrobogrammatic(69), True)
        self.assertEqual(sol.isStrobogrammatic(88), True)
        self.assertEqual(sol.isStrobogrammatic(8008), True)
        self.assertEqual(sol.isStrobogrammatic(8698), True)
        self.assertEqual(sol.isStrobogrammatic(1691), True)

        self.assertEqual(sol.isStrobogrammatic(818), True)
        self.assertEqual(sol.isStrobogrammatic(916), True)
        self.assertEqual(sol.isStrobogrammatic(986), True)
        self.assertEqual(sol.isStrobogrammatic(101), True)
        self.assertEqual(sol.isStrobogrammatic(609), True)

        self.assertEqual(sol.isStrobogrammatic(8), True)

if __name__ == '__main__':
    unittest.main()