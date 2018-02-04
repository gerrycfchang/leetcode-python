"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            result = result + nums[i]

        sum = ((len(nums)+1) * (len(nums))) / 2

        return sum - result
