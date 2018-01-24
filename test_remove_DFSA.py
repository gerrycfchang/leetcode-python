from unittest import TestCase
import unittest
from remove_duplicate_from_sorted_array import Solution


class TestSolution(TestCase):
    def test_removeDuplicates(self):
        sol = Solution()
        self.assertEqual(sol.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(sol.removeDuplicates([1, 1, 2, 2, 3, 4]), 4)
        self.assertEqual(sol.removeDuplicates([1]), 1)
        self.assertEqual(sol.removeDuplicates([1, 2]), 2)
        self.assertEqual(sol.removeDuplicates([]), 0)
        self.assertEqual(sol.removeDuplicates([1, 1]), 1)
        self.assertEqual(sol.removeDuplicates([1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()
