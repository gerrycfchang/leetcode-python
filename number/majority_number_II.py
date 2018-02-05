"""
Given an integer array of size n, find all elements that appear more than  n/3  times. The algorithm should run in linear time and in O(1) space.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1, num2, c1, c2, result = None, None, 0, 0, []

        if len(nums) == 0: return result

        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
            elif c1 == 0:
                num1 = num
                c1 += 1
            elif c2 == 0:
                num2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        for n in [num1, num2]:
            if n is not None and nums.count(n) > len(nums) / 3:
                result.append(n)

        return result
