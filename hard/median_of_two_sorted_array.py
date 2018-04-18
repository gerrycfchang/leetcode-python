# 4. Median of Two Sorted Arrays
# 
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()        
        if len(nums1) % 2 == 0:
            medium = (float(nums1[len(nums1)//2 -1] + nums1[len(nums1)//2])/2)
        else:
            medium = float(nums1[len(nums1)//2])            
        return medium


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([1,3], [2]) == 2.0