class Solution(object):
    def longestCommonSubsequence(self, s1, s2):
        m = len(s1)
        n = len(s2)
        longestStr = []
        dp = [[0 for _ in range(n+1)] for _ in range (m+1)]
        for i in range (m+1):
            dp[i][0] = 0
        for j in range (n+1):
            dp[0][j] = 0

        for i in range (1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif s1[i-1] != s2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

if __name__ == '__main__':
    test = Solution()
    assert test.longestCommonSubsequence('abc','ac') == 2
    assert test.longestCommonSubsequence('13456778','357486782') == 5