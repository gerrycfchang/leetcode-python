"""Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        nums.sort()
        dict, res = {}, set()
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) not in dict:
                    dict[nums[i] + nums[j]] = [(i,j)]
                else:
                    dict[nums[i] + nums[j]].append([i,j])
        for i in range(len(nums)):
            for j in range(i+1, len(nums) - 2):
                t = target-(nums[i]+nums[j])
                if t in dict:
                    for k in dict[t]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
                        
        return [list(i) for i in res]
                    
if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    sol = Solution()
    exp = [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]
    res = sol.fourSum(nums, 0)
    res.sort()
    exp.sort()
    assert res == exp