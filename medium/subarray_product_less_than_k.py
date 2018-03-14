# 713. Subarray Product Less Than K
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def dfs(nums, i, k, value, res):
            if i >= len(nums) or value * nums[i] >= k:
                reslist.append(res)
                res = []
                return
            else:
                res.append(nums[i])
                dfs(nums, i+1, k, value* nums[i], res)
        reslist = []
        for i in range(len(nums)):
            if nums[i] < k:
                reslist.append([nums[i]])
                dfs(nums, i + 1, k, nums[i], [nums[i]])
        return len(reslist)

    def numSubarrayProductLessThanKSol(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        start, prod, cnt = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and prod*nums[end] >= k:
                prod = prod/nums[start]
                start += 1
            prod = 1 if start > end else prod*nums[end]
            cnt = cnt if start > end else cnt+(end-start+1)
        return cnt
                    

if __name__ == '__main__':
    sol = Solution()
    assert sol.numSubarrayProductLessThanKSol([10, 5, 2, 6], 100) == 8 
    assert sol.numSubarrayProductLessThanKSol([10, 5, 2, 7], 14) == 5
    assert sol.numSubarrayProductLessThanK([], 1) == 0
