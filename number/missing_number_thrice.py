class Solution(object):
    def findMissingNumber(self, nums):
        sum = 0
        for i in range (len(nums)):
            sum += nums[i]

        length = len(nums)

        result = ((nums[0] + nums[length-1]) * (nums[length-1] - nums[0] + 1)) / 2 * 3

        return result - sum