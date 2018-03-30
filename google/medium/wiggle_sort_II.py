# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# 
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?# 

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
                nums[i-1], nums[i] = nums[i], nums[i-1]
        

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 5, 2, 1, 6, 4]
    sol.wiggleSort(nums) 
    assert nums == [3, 5, 1, 6, 2, 4]

    nums = [1,2,2,1,2,1,1,1,1,2,2,2]
    sol.wiggleSort(nums)
    assert nums == [1,2,1,2,1,2,1,2,1,2,1,2]