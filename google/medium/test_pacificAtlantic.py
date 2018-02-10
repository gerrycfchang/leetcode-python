from unittest import TestCase
import unittest
from pacific_atlantic import Solution

class TestSolution(TestCase):
    def test_pacificAtlanticCase1(self):
        sol = Solution()

        matrix = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]

        result = sol.pacificAtlantic(matrix)
        exp = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertListEqual(result, exp)
        print result

if __name__ == '__main__':
    unittest.main()