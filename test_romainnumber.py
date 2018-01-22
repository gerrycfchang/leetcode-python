from unittest import TestCase
from roman_to_integer import Solution
import unittest

class TestSolution(TestCase):
    def test_romanToInt(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt('III'),3)
        self.assertEqual(sol.romanToInt('XII'), 12)
        self.assertEqual(sol.romanToInt('XCIX'), 99)
        self.assertEqual(sol.romanToInt('MDCCC'), 1800)
        self.assertEqual(sol.romanToInt('MMMCCCXXXIII'), 3333)
        self.assertEqual(sol.romanToInt('D'), 500)
        self.assertEqual(sol.romanToInt('MCMXCVI'), 1996)

if __name__ == '__main__':
    unittest.main()
