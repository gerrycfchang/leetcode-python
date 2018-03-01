"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return
    def mergeSol(self, nums1, m, nums2, n):
        pIdx = len(nums1) - 1
        while m > 0 and n > 0 :
            if nums1[m-1] > nums2[n-1]:
                nums1[pIdx] = nums1[m-1]                
                m -= 1
                pIdx -= 1
            else:
                nums1[pIdx] = nums2[n-1]
                n -= 1
                pIdx -= 1
        while (n > 0):
            nums1[pIdx] = nums2[n-1]
            n -= 1
            pIdx -= 1

        while (m  > 0):
            nums1[pIdx] = nums1[m-1]
            m -= 1
            pIdx -= 1

            

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 0]
    nums2 = [2]
    sol.mergeSol(nums1, 1, nums2, 1)
    assert (nums1 == [1,2])

    nums1 = [2, 0]
    nums2 = [1]
    sol.mergeSol(nums1, 1, nums2, 1)
    assert (nums1 == [1,2])

    nums1 = [0]
    nums2 = [1]

    sol.mergeSol(nums1, 0, nums2, 1)
    assert (nums1 == [1])

    