"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        while length <= len(nums)-1:
            if nums[length] == val:
                nums.remove(nums[length])
            else:
                length = length + 1

        return len(nums)

if __name__ == '__main__':
    sol = Solution()

    assert(sol.removeElement([2, 3, 3, 4], 3) == 2)
    assert(sol.removeElement([], 1) == 0)