from remove_element import Solution
from unittest import TestCase
import unittest

class TestSolution(TestCase):
    def test_removeElement(self):
        sol = Solution()
        self.assertEqual(sol.removeElement([2, 3, 3, 4], 3), 2)
        self.assertEqual(sol.removeElement([], 1), 0)


if __name__ == '__main__':
    unittest.main()