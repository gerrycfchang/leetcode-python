from unittest import TestCase
import unittest
from remove_kth_digits import Solution


class TestSolution(TestCase):
    def test_removeKthDigitsCase1(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('1432219',3), '1219')

    def test_removeKthDigitsCase2(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('123456',3), '123')

    def test_removeKthDigitsCase3(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('10200',1), '200')

    def test_removeKthDigitsCase4(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('10',2), '0')

    def test_removeKthDigitsCase5(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('10',1), '0')

    def test_removeKthDigitsCase6(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('1173',2), '11')

    def test_removeKthDigitsCase7(self):
        sol = Solution()

        self.assertEqual(sol.removeKdigits('1234567890',9), '0')

if __name__ == '__main__':
    unittest.main()