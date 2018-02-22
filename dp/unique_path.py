"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range (m)]
        for i in range (m):
            dp [i][0] = 1
        for j in range (n):
            dp [0][j] = 1
        
        for i in range (1, m):
            for j in range (1, n):
                dp [i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
            
if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePaths(1, 2) == 1
    assert sol.uniquePaths(2, 1) == 1
    assert sol.uniquePaths(5, 5) == 70