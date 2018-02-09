class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        ### Solution 1:
        #cost = self.loopSolve(dp, n)

        #""" Solution 2
        cost  = self.solve(dp, 1, n)
        #"""

        self.print_path(dp, 1, n)
        return cost

    def loopSolve(self, dp, n):
        for i in range(2, n + 1):
            for j in range(i - 1, -1, -1):
                global_min = 9999
                for k in range(j + 1, i):
                    local_max = k + max(dp[j][k - 1], dp[k + 1][i])
                    global_min = min(local_max, global_min)
                if j + 1 == i:
                    dp[j][i] = j
                else:
                    dp[j][i] = global_min
        return dp[1][n]

    def solve(self, dp, L, R):
        if L >= R: return 0
        if dp[L][R]: return dp[L][R]

        minCost = L + max(self.solve(dp, L, L-1), self.solve(dp, L + 1, R))
        for k in range(L+1, R + 1):
            temp = k + max(self.solve(dp, L, k - 1), self.solve(dp, k + 1, R))
            if temp < minCost:
                minCost = temp
        dp[L][R] = minCost

        #dp[L][R] = min(k + max(self.solve(dp, L, k - 1), self.solve(dp, k + 1, R)) for k in range(L, R + 1))
        return dp[L][R]

    def print_path(self, dp, L, R):
        if L >= R: return
        for i in range(L, R + 1):
            if dp[L][R] == i + max(dp[L][i - 1], dp[i + 1][R]):
                print i
                if dp[L][i - 1] > dp[i + 1][R]:
                    self.print_path(dp, L, i - 1)
                else:
                    self.print_path(dp, i + 1, R)
                break
