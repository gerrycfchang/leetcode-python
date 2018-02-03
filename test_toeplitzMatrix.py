from unittest import TestCase
import unittest
from toeplitz_matrix import Solution


class TestSolution(TestCase):
    def test_toeplitzMatrixCase1(self):
        sol = Solution()

        self.assertEqual(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]),True)

    def test_toeplitzMatrixCase2(self):
        sol = Solution()

        self.assertEqual(sol.isToeplitzMatrix([[1,2],[2,2]]),False)

if __name__ == '__main__':
    unittest.main()