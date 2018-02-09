from unittest import TestCase
import unittest
from game_of_life import Solution

class TestSolution(TestCase):
    def test_gameOfLiveCase1(self):
        sol = Solution()
        res = [[]]
        sol.gameOfLife(res)
        exp = [[]]

        self.assertListEqual(res, exp)

    def test_gameOfLiveCase2(self):
        sol = Solution()
        res = [[1]]
        sol.gameOfLife(res)
        exp = [[0]]

        self.assertListEqual(res, exp)

    def test_gameOfLiveCase3(self):
        sol = Solution()
        res = [[1, 1], [1, 0]]
        sol.gameOfLife(res)
        exp = [[1, 1], [1, 1]]

        self.assertListEqual(res, exp)

    def test_gameOfLiveCase4(self):
        sol = Solution()
        res = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        sol.gameOfLife(res)
        exp = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

        self.assertListEqual(res, exp)


if __name__ == '__main__':
    unittest.main()