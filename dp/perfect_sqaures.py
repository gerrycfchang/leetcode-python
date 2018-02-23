"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### Solution 1
        import math
        if n == 0: return 0
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        squares = [i ** 2 for i in range(1, int(math.sqrt(n)+1))]
        for i in range (1, n+1):
            for j in range(len(squares)):
                sq = squares[j]
                if sq == i:
                    dp[i] = 1
                elif sq <= i:
                    dp[i] = min(dp[i], dp[sq]+dp[i-sq])
                else:
                    break
        return dp[n]

    ### Solution 2
    def numSquaresSol(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### Solution 1
        import math
        if n == 0: return 0
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        squares = [i ** 2 for i in range(1, int(math.sqrt(n)+1))]
        for i in range (1, n+1):
            for j in range(len(squares)):
                if squares[j] <= i:
                    dp[i] = min(dp[i], dp[i-squares[j]]+1)
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    assert sol.numSquares(12) == 3
    assert sol.numSquaresSol(12) == 3
    assert sol.numSquares(13) == 2
    assert sol.numSquares(6922) == 2