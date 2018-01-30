from unittest import TestCase
import unittest
from pascal_triangle import Solution

class TestSolution(TestCase):
    def test_pascalCase1(self):
        sol = Solution()
        exp = [[1],[1,1],[1,2,1],[1,3,3,1]]
        self.assertListEqual(sol.generate(4), exp)

    def test_pascalCase2(self):
        sol = Solution()
        exp = [[1]]
        self.assertListEqual(sol.generate(1), exp)


if __name__ == '__main__':
    unittest.main()