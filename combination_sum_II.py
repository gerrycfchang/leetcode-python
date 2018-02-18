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