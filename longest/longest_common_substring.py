class Solution(object):
    def longestCommonSubstring(self, s1, s2):
        maxLen = 0
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    maxLen = max(maxLen, dp[i][j])
                else:
                    dp[i][j] = 0
        return maxLen

if __name__ == '__main__':
    sol = Solution()
    assert sol.longestCommonSubstring('HISH', 'FISH') == 3
    assert sol.longestCommonSubstring('vista', 'hish') == 2
    assert sol.longestCommonSubstring('fosh', 'fort') == 2