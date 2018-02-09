from unittest import TestCase
import unittest
from flip_game_II import Solution

class TestSolution(TestCase):
    def test_flipGameIICase1(self):
        sol = Solution()

        self.assertEqual(sol.canWin('-++-++-'), False)

    def test_flipGameIICase2(self):
        sol = Solution()

        self.assertEqual(sol.canWin('-++-++-++'), True)

    def test_flipGameIICase3(self):
        sol = Solution()

        self.assertEqual(sol.canWin('-++++-'), True)

    def test_flipGameIICase4(self):
        sol = Solution()

        self.assertEqual(sol.canWin(''), False)

    def test_flipGameIICase5(self):
        sol = Solution()

        self.assertEqual(sol.canWin('-+++--++'), False)


if __name__ == '__main__':
    unittest.main()
