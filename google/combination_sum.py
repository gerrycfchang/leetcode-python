"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        ### Solution 1
        dp = [[] for i in xrange(target + 1)]
        dp[0].append([]) # dp[0] must have content, an empty list, i.e. dp[0] = [[]]
        candidates.sort()
        for i in xrange(1, target + 1):
            for num in candidates:
                if num > i: break
                for item in dp[i-num]:
                    tmp = sorted(item + [num])
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
        return dp[target]
        """
        Solution.ret = []
        self.dfs(sorted(candidates), target, [])
        return Solution.ret


    def dfs(self, candidates, target, valuelist):
        if target == 0 and sorted(valuelist) not in sorted(Solution.ret):
            Solution.ret.append(valuelist)

        for i in range(len(candidates)):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], valuelist + [candidates[i]])

if __name__ == '__main__':
    sol = Solution()

    nums = [2,3,6,7]
    exp = [[2,2,3],[7]]
    assert (sol.combinationSum(nums, 7) == exp)

    nums = [8, 7, 4, 3]
    exp = [[3,4,4],[3,8],[4,7]]
    assert (sol.combinationSum(nums, 11) == exp)
