# 673. Number of Longest Increasing Subsequence
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
#Example 1:
#Input: [1,3,5,4,7]
#Output: 2
#Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
#Example 2:
#Input: [2,2,2,2,2]
#Output: 5
#Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
#Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
#


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [length, count]
        dp = [[1, 1] for i in range(len(nums))]
        max_for_all = 1
        for i in range(len(nums)):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0 
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_len, max_for_all)
        return sum([item[1] for item in dp if item[0] == max_for_all])

if __name__ == '__main__':
    sol = Solution()
    assert sol.findNumberOfLIS([]) == 0
    assert sol.findNumberOfLIS([1]) == 1
    assert sol.findNumberOfLIS([4, 3, 2, 1, 8]) == 4
    assert sol.findNumberOfLIS([2, 1]) == 2
    assert sol.findNumberOfLIS([1,3,5,4,7]) == 2
    assert sol.findNumberOfLIS([2,2,2,2,2]) == 5
    assert sol.findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3