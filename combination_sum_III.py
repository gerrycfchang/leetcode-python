"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]
"""

class Solution(object):
    def combinationSumIII(self, k, n):
        Solution.ret = []
        self.dfs(k, n, 1, [])
        return Solution.ret


    def dfs(self, k, taget, start, valuelist):
        if k == 0 and taget == 0 and valuelist not in Solution.ret:
            Solution.ret.append(valuelist)
        for i in range (start, 10):
            if taget < i:
                return
            self.dfs(k - 1, taget - i, i + 1, valuelist + [i])