"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) >= len(nums2):
            store = nums1
            base = nums2
        else:
            store = nums2
            base = nums1

        for i in range(len(base)):
            if base[i] in store:
                p = store.index(base[i])
                result.append(base[i])
                store[p] = None
        return result

if __name__ == '__main__':
    sol = Solution()
    assert (sol.intersect([],[]) == [])
    assert (sol.intersect([1, 2, 2, 3],[2, 2]) == [2, 2])