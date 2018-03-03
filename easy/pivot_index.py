"""

"""
class Solution(object):
    def pivotIndexSol(self, nums):
        pivot = -1
        length = len(nums)
        if length == 0: return pivot
        i, leftSum, rightSum = 1, [0 for _ in range(length)], [0 for _ in range(length)]
        leftSum[0] = nums[0]
        rightSum[length - 1] = nums[length - 1]
        while i < length:
            leftSum[i] = nums[i] + leftSum[i-1]
            rightSum[length - 1 - i] = nums[length - 1 - i] + rightSum[length - i]
            i += 1

        for i in range(length):
            if leftSum[i] == rightSum[i]:
                pivot = i
                break
        return pivot

if __name__ == '__main__':
    sol = Solution()
    nums = [1,7,3,6,5,6]
    assert sol.pivotIndexSol(nums) == 3

    nums = [-1,-1,-1,-1,-1,-1]
    assert sol.pivotIndexSol(nums) == -1

    nums = [-1,-1,-1,-1,-1,0]
    assert sol.pivotIndexSol(nums) == 2

    nums = [-1,-1,-1,-1,0,-1]
    assert sol.pivotIndexSol(nums) == 2

    nums = [-1,-1,-1,0,-1,-1]
    assert sol.pivotIndexSol(nums) == 2

    nums = [-1,-1,-1,0,1,1]
    assert sol.pivotIndexSol(nums) == 0
