from unittest import TestCase
import unittest
from h_index import Solution

class TestSolution(TestCase):
    def test_hIndexCase1(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([3, 0, 6, 1, 5]), 3)

    def test_hIndexCase2(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([]), 0)

    def test_hIndexCase3(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([0]), 0)

    def test_hIndexCase4(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([100]), 1)

    def test_hIndexCase5(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([0, 1]), 1)



if __name__ == '__main__':
    unittest.main()