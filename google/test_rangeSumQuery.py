from unittest import TestCase
import unittest
from range_sum_query import NumMatrix


class TestSolution(TestCase):
    def test_randomSumQueryCase1(self):

        """
        input = matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]
        """
        input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        matrix = NumMatrix(input)

        self.assertEqual(matrix.sumRegion(1, 1, 2, 2),28)


if __name__ == '__main__':
    unittest.main()