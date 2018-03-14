# 674. Longest Continuous Increasing Subsequence
#
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, 
# it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] + 1 if nums[i] > nums[i-1] else 1
        return max(dp)
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.findLengthOfLCIS([1,3,5,4,7]) == 3