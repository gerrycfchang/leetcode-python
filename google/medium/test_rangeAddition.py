from unittest import TestCase
import unittest
from range_addition import Solution

class TestSolution(TestCase):
    def test_rangeAdditionCase1(self):
        sol = Solution()

        updates = [
            [1, 3, 2],
            [2, 4, 3],
            [0, 2, -2]
        ]
        result = sol.getModifiedArray(5, updates)
        self.assertListEqual(result , [-2, 0, 3, 5, 3])

    def test_rangeAdditionCase2(self):
            sol = Solution()

            updates = [
                [1, 3, 2],
                [2, 4, 3],
                [0, 2, -2]
            ]
            result = sol.getModifiedArray(0, updates)
            self.assertListEqual(result, [])

    def test_rangeAdditionCase3(self):
            sol = Solution()

            updates = [
                [0, 0, 1]
            ]

            result = sol.getModifiedArray(1, updates)
            self.assertListEqual(result, [1])

if __name__ == '__main__':
    unittest.main()

