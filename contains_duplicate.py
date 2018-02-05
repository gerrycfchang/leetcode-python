"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,

and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0: return False
        table = {}
        for num in nums:
            if not (num in table):
                table[num] = 1
            else:
                table[num] += 1

        return len(table) != len(nums)