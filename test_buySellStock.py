from unittest import TestCase
import unittest
from buy_sell_stock import Solution


class TestSolution(TestCase):
    def test_buySellStockCase1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_buySellStockCase2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([]), 0)

    def test_buySellStockCase3(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([1, 4, 2]), 3)


if __name__ == '__main__':
    unittest.main()
