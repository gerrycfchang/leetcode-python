# 628. Maximum Product of Three Numbers
# 
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
# 
# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProduct, n = float('-inf'), len(nums)
        for i in range (n-2):
            for j in range(i+1, n-1):
                for k in reversed(range(j+1, n)):
                    tmp = (nums[i] * nums[j] * nums[k])
                    maxProduct = max(maxProduct, tmp)
        return maxProduct

    def anotherMaxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumProduct([1, 2, 3]) == 6
    assert sol.anotherMaxProduct([1, 2, 3]) == 6