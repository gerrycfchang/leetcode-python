"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range (len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])        
        return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    sol = Solution()
    assert sol.lengthOfLIS(nums) == 4
    assert sol.lengthOfLIS([]) == 0
    assert sol.lengthOfLIS([3]) == 1
