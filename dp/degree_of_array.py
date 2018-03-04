"""
697. Degree of an Array

Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = [1 for _ in range(m)]
        table = {}
        table[nums[0]] = [1, 0]
        maxdegree = 1
        
        for i in range(1,m):
            if nums[i] not in table:
                table[nums[i]] = [1, i]
                dp[i] = dp[i-1]
            else:
                table[nums[i]][0] += 1
                length = i - table[nums[i]][1] + 1
                if table[nums[i]][0] > maxdegree:
                    maxdegree = table[nums[i]][0]
                    dp[i] = length 
                elif table[nums[i]][0] == maxdegree:
                    dp[i] = min(dp[i-1], length)
                else:
                    dp[i] = dp[i-1]
        return dp[m-1]
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 3, 1]
    assert sol.findShortestSubArray(nums) == 2

    nums = [1,2,2,3,1,4,2]
    assert sol.findShortestSubArray(nums) == 6

    nums = [0]
    assert sol.findShortestSubArray(nums) == 1

    nums = [6,6,6,7,7]
    assert sol.findShortestSubArray(nums) == 3