from unittest import TestCase
import unittest
from first_unique_char import Solution


class TestSolution(TestCase):
    def test_firstUniqueCharCase1(self):
        sol = Solution()
        self.assertEqual(sol.firstUniqChar('leetcode'), 0)

if __name__ == "__main__":
    unittest.main()
