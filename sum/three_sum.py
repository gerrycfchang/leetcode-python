"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    ### Solution 1: AC
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    comb = [nums[i], nums[l], nums[r]]
                    res.append(comb)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while r > l and nums[r] == nums[r+1]: r -= 1
                    
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return res

    ### Solution 2: Time limit exceeded
    def threeSumSol2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        dict, res = {}, set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j]) not in dict:
                    dict[nums[i]+nums[j]] = [(i,j)]
                else:
                    dict[nums[i]+nums[j]].append([i,j])
                    
        for i in range(len(nums)-1):
            target = 0 - nums[i]
            if target in dict:
                for k in dict[target]:
                    if k[0] > i:
                        res.add((nums[i], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]

    ### Solution 3: Time limit exceeded
    def threeSumSol3(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range (len(nums) -2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    comb = [nums[i], nums[l], nums[r]]
                    if comb not in res:
                        res.append(comb)
                    l += 1
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return res

                
                
if __name__ == '__main__':        
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    exp = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    res = sol.threeSum(nums)
    res.sort()
    exp.sort()
    assert res == exp

    res = sol.threeSumSol2(nums)
    res.sort()
    exp.sort()
    assert res == exp

    res = sol.threeSumSol3(nums)
    res.sort()
    exp.sort()
    assert res == exp