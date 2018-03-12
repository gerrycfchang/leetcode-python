import collections
class Solution(object):
    def longestRepeatedSubseq(self, s):
        n, res = len(s), []
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for size in range(2, n+1):
            for i in range(n-size+1):
                j = i + size -1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 1
                else:
                    for k in range(i, j+1):
                        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])
        return dp[0][n-1]

    def findLongestRepeatingSubSeq(self, str):
        n = len(str)
    
        # Create and initialize DP table
        dp = [[0 for k in range(n+1)] for l in range(n+1)]
    
        # Fill dp table (similar to LCS loops)
        for i in range(1, n+1):
            for j in range(1, n+1):
                # If characters match and indices are not same
                if (str[i-1] == str[j-1] and i != j):
                    dp[i][j] = 1 + dp[i-1][j-1]
    
                # If characters do not match
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
        return dp[n][n]

if __name__ == '__main__':
    sol = Solution()
    assert sol.findLongestRepeatingSubSeq('aabb') == 2
    assert sol.findLongestRepeatingSubSeq('aabb') == 2
    assert sol.findLongestRepeatingSubSeq('aabbb') == 2
    assert sol.longestRepeatedSubseq('aab') == 1
    assert sol.longestRepeatedSubseq('aabebcdd') == 3
    assert sol.longestRepeatedSubseq('acac') == 1
    assert sol.longestRepeatedSubseq('cabbc') == 5