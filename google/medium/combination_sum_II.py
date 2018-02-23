"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSumII(self, candidates, target):
        Solution.ret = []
        self.dfs(sorted(candidates), 0, target, [])
        return Solution.ret

    def dfs(self, candidates, start, target, valuelist):
        if target == 0 and valuelist not in Solution.ret:
            Solution.ret.append(valuelist)

        for i in range (start, len(candidates)):
            if target < candidates[i]:
                return
            self.dfs(candidates, i + 1, target - candidates[i], valuelist + [candidates[i]])

if __name__ == '__main__':
    sol = Solution()

    nums = [10, 1, 2, 7, 6, 1, 5]
    exp = [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
        ]
    assert (sorted(sol.combinationSumII(nums, 8)) == sorted(exp))