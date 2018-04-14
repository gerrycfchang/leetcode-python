# 611. Valid Triangle Number
# 
# Given an array consists of non-negative integers, 
# your task is to count the number of triplets chosen from the array 
# that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] > nums[k]:
                        res += 1
                    else:
                        break
        return res

    def triangleNumberSol(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] <= nums[i]:
                    k -= 1
                else:
                    res += k-j
                    j += 1
        return res
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.triangleNumber([2,2,3,4]) == 3
    assert sol.triangleNumberSol([2,2,3,4]) == 3