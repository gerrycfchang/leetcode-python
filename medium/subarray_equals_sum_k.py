# 560. Subarray Sum Equals K
# 
# Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, total, dic = 0, 0, {0:1}
        for num in nums:
            total += num
            res += dic.get(total-k, 0)
            dic[total] = dic.get(total,0) + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 2, 1], 3) == 2
        