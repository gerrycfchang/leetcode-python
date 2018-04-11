# 33. Search in Rotated Sorted Array
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return -1 if target not in nums else nums.index(target)
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.search([4,5,6,7,0,1,2], 5) == 1
    assert sol.search([4,5,6,7,0,1,2], 8) == -1