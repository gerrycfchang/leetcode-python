from unittest import TestCase
from sort import BubbleSort
from sort import QuickSort
from sort  import InsertionSort
import unittest


class TestSolution(TestCase):
    def test_bubbleSortCase1(self):
        obj = BubbleSort()
        nums = [4, 2, 6, 1]
        obj.sort(nums)
        self.assertListEqual(nums, [1, 2, 4, 6])

    def test_bubbleSortCase2(self):
        obj = BubbleSort()
        nums = [4, 24, 6, 1, 17, 3, 89, 43, 45]
        obj.sort(nums)
        self.assertListEqual(nums, [1, 3, 4, 6, 17, 24, 43, 45, 89])


    def test_quickSortCase1(self):
        obj = QuickSort()
        nums = [4, 2, 6, 1, 7, 3]
        obj.sort(nums, 0, 5)
        self.assertListEqual(nums, [1, 2, 3, 4, 6, 7])

    def test_quickSortCase2(self):
        obj = QuickSort()
        nums = [4, 24, 6, 1, 17, 3, 89, 43, 45]
        obj.sort(nums, 0, 8)
        self.assertListEqual(nums, [1, 3, 4, 6, 17, 24, 43, 45, 89])

    def test_insertionSortCase1(self):
        obj = InsertionSort()
        nums = [4, 2, 6, 1, 7, 3]
        obj.sort(nums)
        self.assertListEqual(nums, [1, 2, 3, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()