from unittest import TestCase
import unittest
from rotate_array import Solution


class TestSolution(TestCase):
    def test_rotateArrayCase1(self):
        sol = Solution()
        nums = [-1]
        sol.rotate(nums, 2)
        self.assertListEqual(nums,[-1])

    def test_rotateArrayCase2(self):
        sol = Solution()
        nums = [1, 2]
        sol.rotate(nums, 1)
        self.assertListEqual(nums, [2, 1])

    def test_rotateArrayCase3(self):
        sol = Solution()
        nums = [1,2,3,4,5,6]
        sol.rotate(nums, 2)
        self.assertListEqual(nums, [5,6,1,2,3,4])

if __name__ == '__main__':
    unittest.main()