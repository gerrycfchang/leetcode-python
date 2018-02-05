from unittest import TestCase
import unittest
from contains_duplicate import Solution

class TestSolution(TestCase):
    def test_containsDuplicateCase1(self):
        sol = Solution()

        self.assertEqual(sol.containsDuplicate([]), False)

    def test_containsDuplicateCase2(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([2, 2, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9]), True)

    def test_containsDuplicateCase3(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1, 2, 3, 4, 5, 6, 7]), False)

if __name__ == '__main__':
    unittest.main()