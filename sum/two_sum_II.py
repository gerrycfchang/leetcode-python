"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSumSol(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            elif total == target:
                return [l+1, r+1]
        return None

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [0, 1]
        dic = {}
        for x in range(0, len(numbers)):
            dic[numbers[x]] = x

        for x in range(0, len(numbers)):
            rest = abs(target - numbers[x])
            if rest in dic:
                result[0] = x+1
                result[1] = dic[rest]+1
                return result

if __name__ == '__main__':
    nums = [5, 10, 13, 30]
    target = 23
    test = Solution()
    assert test.twoSum(nums, target) == [2, 3]

    assert test.twoSumSol(nums, target) == [2, 3]
    
