# 730. Count Different Palindromic Subsequences
# 
# Given a string S, find the number of different non-empty palindromic subsequences in S, 
# 
# and return that number modulo 10^9 + 7.
# 
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
# 
# A sequence is palindromic if it is equal to the sequence reversed.
# 
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
# 
# Example 1:
# Input: 
# S = 'bccb'
# Output: 6
# Explanation: 
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.# 


class Solution:
    def countPalindromicSubsequences(self, S):        
        n = len(S)
        if n == 0: return 0        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
            
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1                
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1] * 2
                    l = i + 1
                    r = j - 1
                    while l <= r and S[l] != S[i]: l += 1
                    while l <= r and S[r] != S[i]: r -= 1
                    if l > r: dp[i][j] += 2
                    elif l == r: dp[i][j] += 1
                    else: dp[i][j] -= dp[l + 1][r - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] 
                #dp[i][j] %= 1000000007
            
        return dp[0][n - 1]
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.countPalindromicSubsequences('bccb') == 6