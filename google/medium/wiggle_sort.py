# 280. Wiggle Sort
# 
# Given an unsorted array nums, 
#
# reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

class Solution(object):
    def wiggleSort(self, nums):
        prev, incr = nums[0], True
        for i in range(1, len(nums)):
            if (incr and prev < nums[i]) or (not incr and prev > nums[i]):
                nums[i - 1] = prev
                prev = nums[i]
            else:
                nums[i-1] = nums[i]
            incr = not incr
        
if __name__ == '__main__':
    sol = Solution()
    nums = [3, 5, 2, 1, 6, 4]
    sol.wiggleSort(nums) 
    assert nums == [3, 5, 1, 6, 2, 4]

    nums = [1,2,2,1,2,1,1,1,1,2,2,2]
    sol.wiggleSort(nums)
    assert nums == [1,2,1,2,1,2,1,2,1,2,1,2]