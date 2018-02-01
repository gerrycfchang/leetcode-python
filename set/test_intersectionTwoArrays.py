from unittest import TestCase
import unittest
from intersection_two_array import Solution

class TestSolution(TestCase):
    def test_intersectionCase1(self):
        sol = Solution()
        self.assertListEqual(sol.intersection([],[]),[])

    def test_intersectionCase2(self):
        sol = Solution()
        self.assertListEqual(sol.intersection([1, 2, 2, 3],[2, 2]),[2])


if __name__ == '__main__':
    unittest.main()
