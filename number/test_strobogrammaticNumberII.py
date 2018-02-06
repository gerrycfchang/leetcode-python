from unittest import TestCase
import unittest
from strobogrammatic_number_II import Solution


class TestSolution(TestCase):
    def test_strobogrammaticNumberIICase1(self):
        sol = Solution()

        exp = ["11","69","88","96"]
        self.assertListEqual(sol.findStrobogrammatic(2), exp)

    def test_strobogrammaticNumberIICase2(self):
        sol = Solution()

        exp = ["101", "609", "808", "906", "111", "619", "818", "916", "181", "689", "888", "986"]
        self.assertListEqual(sol.findStrobogrammatic(3), exp)

    def test_strobogrammaticNumberIICase3(self):
        sol = Solution()

        exp = ["1001", "6009", "8008", "9006", "1111", "6119", "8118", "9116", "1691", "6699",
               "8698", "9696", "1881", "6889", "8888", "9886", "1961", "6969", "8968", "9966"]
        self.assertListEqual(sol.findStrobogrammatic(4), exp)


if __name__ == '__main__':
    unittest.main()