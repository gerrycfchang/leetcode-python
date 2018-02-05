from unittest import TestCase
import unittest
from count_primes import Solution

class TestSolution(TestCase):
    def test_countPrimesCase1(self):
        sol = Solution()
        self.assertEqual(sol.countPrimes(8), 4)

    def test_countPrimesCase2(self):
        sol = Solution()
        self.assertEqual(sol.countPrimes(26), 9)

if __name__ == '__main__':
    unittest.main()