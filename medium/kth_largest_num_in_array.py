# 215. Kth Largest Element in an Array
# 
# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5 