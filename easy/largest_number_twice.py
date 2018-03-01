"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        idx = 0
        isDouble = True
        for i in range(1, len(nums)):
            if nums[i] > nums[idx]:
                idx = i
        
        for i in range (len(nums)):
            if nums[idx] < 2 * nums[i]:
                if i == idx:
                    continue
                isDouble = False
                break
            
        return -1 if not isDouble else idx

if __name__ == '__main__':
    sol = Solution()
    assert sol.dominantIndex([0, 0, 0, 1]) == 3
    assert sol.dominantIndex([3, 6, 1, 0]) == 1
    assert sol.dominantIndex([1, 2, 3, 4]) == -1
    assert sol.dominantIndex([1]) == 0
    assert sol.dominantIndex([1, 0]) == 0
    assert sol.dominantIndex([0, 2, 3, 0]) == -1
