"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,

and it should return false if every element is distinct.

"""

import collections
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

    def containsDuplicateSol(self, nums):
        c = collections.Counter()
        for num in nums:
            c[num] += 1
        return len(c) != len(nums)

if __name__ == '__main__':
    sol = Solution()

    assert (sol.containsDuplicate([]) == False)
    assert (sol.containsDuplicate([2, 2, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9]) == True)
    assert (sol.containsDuplicateSol([2, 2, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9]) == True)
    assert (sol.containsDuplicate([1, 2, 3, 4, 5, 6, 7]) == False)