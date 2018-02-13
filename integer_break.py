"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2 or n==3: return n -1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
        """
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            maxnum = 0
            for j in range(1, (i>>1)+1):
                maxnum = max(max(dp[j], j) * max(dp[i-j],i-j), maxnum)
            dp[i] = maxnum
        return dp[n]
        """
        