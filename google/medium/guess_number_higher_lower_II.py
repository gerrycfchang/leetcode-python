class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        ### Solution 1:
        cost = self.loopSolve(dp, n)

        #""" Solution 2
        #cost  = self.solve(dp, 1, n)
        #"""

        self.print_path(dp, 1, n)
        return cost

    def loopSolve(self, dp, n):
        for L in range(n-1, 0, -1):
            for R in range(L + 1, n+1):
                dp[L][R] = float('inf')
                for i in range(L, R):
                    dp[L][R] = min(dp[L][R], i + max(dp[L][i - 1], dp[i + 1][R]))
        return dp[1][n]

    def solve(self, dp, L, R):
        if L >= R: return 0
        if dp[L][R]: return dp[L][R]
        dp[L][R] = float('inf')
        for i in range(L, R+1):
            dp[L][R] = min(dp[L][R], i + max(self.solve(dp,L,i-1),self.solve(dp,i+1,R)))
        
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

if __name__ == '__main__':
    sol = Solution()
    assert (sol.getMoneyAmount(4) == 4)
