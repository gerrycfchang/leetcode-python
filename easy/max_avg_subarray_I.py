# 643. Maximum Average Subarray I
# 
# Given an array consisting of n integers, find the contiguous subarray of 
# 
# given length k that has the maximum average value. And you need to output the maximum average value.
# 
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) <= k: return float(sum(nums))/k
        sumList = [0] * len(nums)
        sumList[k-1] = sum(nums[:k])
        j = 0
        for i in range(k, len(nums)):
            sumList[i] = sumList[i-1] + nums[i] - nums[j]
            j += 1
        return float(max(sumList[k-1:]))/k
            
if __name__ == '__main__':
    sol = Solution()
    nums = [1,12,-5,-6,50,3]
    assert sol.findMaxAverage(nums, 4) == 12.75

    nums = [0,4,0,3,2]
    assert sol.findMaxAverage(nums, 1) == 4.0