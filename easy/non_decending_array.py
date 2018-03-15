# 665. Non-decreasing Array
#
# Given an array with n integers, your task is to check 
# 
# if it could become non-decreasing by modifying at most 1 element.
# 
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# 
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1 or ((i-1 >= 0 and nums[i-1] > nums[i+1]) and (i+2 < len(nums) and nums[i+2] < nums[i]) ):
                    return False
        return True
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.checkPossibility([4, 2, 3]) == True
    assert sol.checkPossibility([4, 2, 1]) == False
    assert sol.checkPossibility([3, 4, 2, 3]) == False