# 525. Contiguous Array
# 
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# 
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, table, maxLen = 0, {0:0}, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                maxLen = max(maxLen, i - table[count] + 1)
            else:
                table[count] = i + 1
        return maxLen


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMaxLength([1,0]) == 2
    assert sol.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4