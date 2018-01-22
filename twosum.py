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
                return result[] = [x, dic[rest]]


if __name__ == '__main__':
    nums = [0, 16, 11, 3]
    target = 3
    test = Solution()
    rlist = test.twoSum(nums, target)
    print rlist
