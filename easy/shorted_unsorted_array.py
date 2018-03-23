# 581. Shortest Unsorted Continuous Subarray
# 
# Given an integer array, you need to find one continuous subarray 
# that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order, too.
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to 
# make the whole array sorted in ascending order.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        leftIdx, rightIdx = 0, 0
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                leftIdx = i
                break
        for i in range(len(nums)-1, -1, -1):  
            if nums[i] != sortedNums[i]:
                rightIdx = i
                break
        return (rightIdx - leftIdx + 1) if rightIdx else 0
                
if __name__ == '__main__':
    sol = Solution()
    assert sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5