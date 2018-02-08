from unittest import TestCase
import unittest
from connected_component import Solution

class TestSolution(TestCase):
    def test_connectedComponentCase1(self):
        sol = Solution()
        edges = [[0, 1], [1, 2], [3, 4]]
        self.assertEqual(sol.countComponents(5, edges), 2)

    def test_connectedComponentCase2(self):
        sol = Solution()
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(sol.countComponents(5, edges), 1)

    def test_connectedComponentCase3(self):
        sol = Solution()
        edges = [[0, 1], [2, 3], [4, 5], [6, 7]]
        self.assertEqual(sol.countComponents(8, edges), 4)


if __name__ == '__main__':
    unittest.main()