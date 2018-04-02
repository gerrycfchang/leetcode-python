# 219. Contains Duplicate II
#
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
#
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for idx, val in enumerate(nums):
            if val in dic and idx - dic[val] <= k:
                return True
            dic[val] = idx
        return False
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.containsNearbyDuplicate([], 0) == False
    assert sol.containsNearbyDuplicate([1, 2, 2, 3, 4], 1) == True

