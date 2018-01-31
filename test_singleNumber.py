from unittest import TestCase
import unittest
from single_number import Solution

class TestSolution(TestCase):
    def test_singleNumberCase1(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([1]),1)

    def test_singleNumberCase2(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([5,3,4,1,3,5,4]),1)

if __name__ == '__main__':
    unittest.main()