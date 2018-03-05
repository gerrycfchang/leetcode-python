# 695. Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical.) # 
# You may assume all four e# dges of the grid are surrounded by water.# 
# 
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
# 
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea, localCount = 0, [0]
        def dfs(grid, i, j, visited):
            m = len(grid)
            n = len(grid[0])
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0: return
            localCount[0] += 1
            visited[i][j] = True
            dfs(grid, i - 1, j, visited)
            dfs(grid, i + 1, j , visited)
            dfs(grid, i, j - 1, visited)
            dfs(grid, i, j + 1, visited)
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                localCount[0] = 0
                dfs(grid, i, j, visited)
                maxArea = max(maxArea, localCount[0])
        return maxArea
        

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 		[0,0,0,0,0,0,0,1,1,1,0,0,0],
 		[0,1,1,0,1,0,0,0,0,0,0,0,0],
 		[0,1,0,0,1,1,0,0,1,0,1,0,0],
 		[0,1,0,0,1,1,0,0,1,1,1,0,0],
 		[0,0,0,0,0,0,0,0,0,0,1,0,0],
 		[0,0,0,0,0,0,0,1,1,1,0,0,0],
 		[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert sol.maxAreaOfIsland(grid) == 6

    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    assert sol.maxAreaOfIsland(grid) == 4

    grid = [[0,0,0,0,0,0,0,0]]
    assert sol.maxAreaOfIsland(grid) == 0