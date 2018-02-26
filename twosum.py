'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for x in range(0, len(nums)):
            dic[nums[x]] = x
            print dic

        for x in range(0, len(nums)):
            rest = abs(target - nums[x])
            print rest
            if rest in dic:
                return [x, dic[rest]]
    
    def twoSumSol(self, nums, target):
        from collections import Counter
        c = Counter()
        for i in range (len(nums)):
            part = target - nums[i]
            if part in c:
                return [c[part], i]
            else:
                c[nums[i]] = i        
        return None


if __name__ == '__main__':
    nums = [0, 16, 11, 3]
    target = 3
    test = Solution()
    assert test.twoSumSol(nums, target) == [0,3]
