"""
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        max_num = [0 for _ in range(m)]
        min_num = [0 for _ in range(m)]
        
        max_num[0] = min_num[0] = nums[0]
        
        for i in range(1,m):
            max_num[i] = min_num[i] = nums[i]
            if nums[i] > 0:
                max_num[i] = max(max_num[i-1] * nums[i], max_num[i])
                min_num[i] = min(min_num[i-1] * nums[i], min_num[i])
            else:
                max_num[i] = max(min_num[i-1] * nums[i], max_num[i])
                min_num[i] = min(max_num[i-1] * nums[i], min_num[i])
        return max(max_num)
        

if __name__ == '__main__':
    sol = Solution()
    nums = [-2]
    assert sol.maxProduct(nums) == -2

    nums = [-2,3,-4]
    assert sol.maxProduct(nums) == 24