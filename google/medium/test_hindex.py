from unittest import TestCase
import unittest
from h_index import Solution

class TestSolution(TestCase):
    def test_hIndexCase1(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([3, 0, 6, 1, 5]), 3)




if __name__ == '__main__':
    unittest.main()