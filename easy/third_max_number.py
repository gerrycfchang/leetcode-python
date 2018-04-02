# 414. Third Maximum Number
# 
# Given a non-empty array of integers, return the third maximum number in this array. 
# If it does not exist, return the maximum number. The time complexity must be in O(n).
# 
# Example 1:
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
# 
# Output: 1


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 = num2 = num3 = float('-inf')
        for i in set(nums):
            if i > num1:
                num3 = num2
                num2 = num1
                num1 = i               
            elif i > num2:
                num3 = num2
                num2 = i
            elif i > num3:
                num3 = i
        return num3 if num3 != float('-inf') else num1

if __name__ == '__main__':
    sol = Solution()
    assert sol.thirdMax([3, 2, 1]) == 1
    assert sol.thirdMax([2, 2, 3, 1]) == 1
    assert sol.thirdMax([2, 1]) == 2