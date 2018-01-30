"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = self.detectNegativeValue(nums)
        if sum < 0:
            return sum

        maxValue = nums[0]
        for i in range(0, len(nums)):
            sum = sum + nums[i]
            sum = max(sum, 0)
            maxValue = max(sum, maxValue)

        return maxValue

    def detectNegativeValue(self, nums):
        maxValue = nums[0]
        for i in range(0, len(nums)):
            if nums[i] < 0:
                if nums[i] > maxValue:
                    maxValue = nums[i]
            else:
                return 0

        return maxValue
