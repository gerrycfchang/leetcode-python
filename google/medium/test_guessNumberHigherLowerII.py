from unittest import TestCase
import unittest
from guess_number_higher_lower_II import Solution

class TestSolution(TestCase):
    def test_guessNumberCase1(self):
        sol = Solution()
        self.assertEqual(sol.getMoneyAmount(4), 4)


if __name__ == '__main__':
    unittest.main()