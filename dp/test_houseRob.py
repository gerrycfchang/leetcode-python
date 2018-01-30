from unittest import TestCase
import unittest

from house_rob import Solution

class TestSolution(TestCase):
    def test_houseRobCase1(self):
        sol = Solution()

        self.assertEqual(sol.rob([1,1,1]),2)

    def test_houseRobCase2(self):
        sol = Solution()

        self.assertEqual(sol.rob([]),0)

if __name__ == '__main__':
    unittest.main()