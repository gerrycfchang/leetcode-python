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
        """
        dp = [[] for i in xrange(target + 1)]
        dp[0].append([]) # dp[0] must have content, an empty list, i.e. dp[0] = [[]]
        for i in xrange(1, target + 1):
            for num in candidates:
                if num > i: break
                for item in dp[i-num]:
                    tmp = sorted(item + [num])
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
        return dp[target]
        