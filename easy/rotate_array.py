"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0 or k == len(nums) or len(nums) == 1:
            return
        if k > len(nums):
            k %= len(nums)

        for i in range (len(nums) - k):
            nums.append(nums[0])
            nums.remove(nums[0])

if __name__ == '__main__':
    sol = Solution()
    nums = [-1]
    sol.rotate(nums, 2)
    assert(nums == [-1])

    nums = [1, 2]
    sol.rotate(nums, 1)
    assert(nums == [2, 1])

    nums = [1,2,3,4,5,6]
    sol.rotate(nums, 2)
    assert(nums == [5,6,1,2,3,4])
