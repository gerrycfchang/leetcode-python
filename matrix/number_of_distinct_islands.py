# 694. Number of Distinct Islands
# 
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands. An island is considered to be the same as another 
# 
# if and only if one island can be translated (and not rotated or reflected) to equal the other.
# 
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# 
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
 
 
import collections
class Solution(object):
    def numDistinctIslands(self, grid):
        m, n, reslist = len(grid), len(grid[0]), []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 1 and not visited[i][j]:
                    res = []
                    self.dfs(grid, i, j, visited, res)
                    reslist.append(sorted(res))
        return self.distinct(reslist)

    def dfs(self, grid, i, j, visited, res):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0: return
        dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        visited[i][j] = True
        res.append(i*n+j)     
        for _dir in dirs:
            self.dfs(grid, i + _dir[0], j + _dir[1], visited, res)
    
    def distinct(self, islands):
        c = collections.Counter()
        for island in islands:
            if island[0] != 0:
                for x in range(1,len(island)):
                    island[x] -= island[0] 
                island[0] = 0
            c[tuple(island)] += 1
        return len(c)        


if __name__ == "__main__":
    sol = Solution()
    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]
    ]
    assert sol.numDistinctIslands(grid) == 1

    grid = [[1,1,0,1,1],
            [1,0,0,0,0],
            [0,0,0,1,1],
            [1,1,0,1,0]
    ]
    assert sol.numDistinctIslands(grid) == 2

    grid = [[1,0,0,1],
            [1,0,1,0]
    ]
    assert sol.numDistinctIslands(grid) == 2
