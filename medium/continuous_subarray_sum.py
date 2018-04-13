# 523. Continuous Subarray Sum
# 
# Given a list of non-negative numbers and a target integer k, 
# write a function to check if the array has a continuous subarray of size 
# at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.
# 
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2 or (sum(nums) > 0 and k == 0): return False
        
        for i in range(len(nums)-1):
            total = nums[i]
            for j in range(i+1, len(nums)):
                total = total + nums[j]
                if k != 0 and total % k == 0:
                    return True
                if k == 0 and total ==0:
                    return True
        return False
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.checkSubarraySum([23, 2, 6, 4, 7], 6) == True
    assert sol.checkSubarraySum([0, 0], 0) == True
    assert sol.checkSubarraySum([0, 1], 0) == False