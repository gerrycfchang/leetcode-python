"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if  nums[i+1] == nums[i]:
                nums.remove(nums[i])
            else:
                i = i + 1

        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    
    assert(sol.removeDuplicates([1, 1, 2]) == 2)
    assert(sol.removeDuplicates([1, 1, 2, 2, 3, 4]) == 4)
    assert(sol.removeDuplicates([1]) == 1)
    assert(sol.removeDuplicates([1, 2]) == 2)
    assert(sol.removeDuplicates([]) == 0)
    assert(sol.removeDuplicates([1, 1]) == 1)
    assert(sol.removeDuplicates([1, 1, 1]) == 1)