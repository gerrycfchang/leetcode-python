from unittest import TestCase
import unittest
from title_to_number import Solution


class TestSolution(TestCase):
    def test_titleToNumberCase1(self):

        sol = Solution()
        self.assertEqual(sol.titleToNumber('A'), 1)

    def test_titleToNumberCase2(self):
        sol = Solution()
        self.assertEqual(sol.titleToNumber('AA'), 27)


if __name__ == '__main__':
    unittest.main()