class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        result = [nums[0]]
        result.append(max(nums[0], nums[1]))
        value = 0
        for i in range(2, len(nums)):
            value = max(result[i - 2] + nums[i], result[i - 1])
            result.append(value)

        return value

if __name__ == '__main__':
    sol = Solution()
    assert (sol.rob([1,1,1]) == 2)
    assert (sol.rob([]) == 0)