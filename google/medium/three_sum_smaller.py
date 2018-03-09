# 259. 3Sum Smaller
# 
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n 
# 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# 
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# 
# Return 2. Because there are two triplets which sums are less than 2:
# 
# [-2, 0, 1]
# [-2, 0, 3]


class Solution(object):
    def threeSumSmaller(self, nums, target):
        Solution.ret, res = [], []
        self.dfs(nums, 0, target, 0, 0, [])
        return len(Solution.ret)

    def dfs(self, nums, start, target, value, count, valuelist):
        if count == 3 and value < target: 
            Solution.ret.append(valuelist)
            return
        for i in range(start, len(nums)):
            #res.append(nums[i])
            self.dfs(nums, i + 1, target, value + nums[i], count+1, valuelist+[nums[i]])

if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 0, 1, 3]
    assert sol.threeSumSmaller(nums, 2) == 2

    nums = [-2, 0, 1, 3]
    assert sol.threeSumSmaller(nums, 9) == 4

    nums = [-2, 0, 1, 3, 5, 2]
    assert sol.threeSumSmaller(nums, 4) == 8