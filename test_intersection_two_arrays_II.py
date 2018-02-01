from unittest import TestCase
import unittest
from intersection_two_arrays_II import Solution


class TestSolution(TestCase):
    def test_intersectionCase1(self):
        sol = Solution()
        self.assertListEqual(sol.intersect([],[]),[])

    def test_intersectionCase2(self):
        sol = Solution()
        self.assertListEqual(sol.intersect([1, 2, 2, 3],[2, 2]),[2, 2])


if __name__ == '__main__':
    unittest.main()
