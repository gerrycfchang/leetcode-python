# 516. Longest Palindromic Subsequence
#
# Given a string s, find the longest palindromic subsequence's length in s. 
# 
# You may assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# 
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
# 
# "cbbd"
# Output:
# 2


class Solution(object):
    def longestPalindromeSubseqFromRight(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return len(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
    
    def longestPalindromeSubseqFromLeft(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return len(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for size in range(2, n+1):
            for i in range(n-size+1):
                j = i + size -1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindromeSubseqFromRight('bbbab') == 4
    assert sol.longestPalindromeSubseqFromLeft('bbbab') == 4
    assert sol.longestPalindromeSubseqFromLeft('cbba') == 2
    assert sol.longestPalindromeSubseqFromLeft('zzzzzzzzzz') == 10
    assert sol.longestPalindromeSubseqFromLeft('abadcaacbddd') == 6