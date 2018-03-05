# 463. Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
#Grid cells are connected horizontally/vertically (not diagonally).
#The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
#The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
#One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.
#
#Example:
#
#[[0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]]
#
#Answer: 16
#Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        edge, count = [0], [0]
        def dfs(matrix, i, j, visited):
            if visited[i][j] or matrix[i][j] == 0: return
            m = len(matrix)
            n = len(matrix[0])
            visited[i][j] = True
            count[0] += 1
            if i > 0 and matrix[i-1][j]: 
                edge[0] += 1
                dfs(matrix, i-1, j, visited)
            if j > 0 and matrix[i][j-1]: 
                edge[0] += 1
                dfs(matrix, i, j-1, visited)
            if i < m - 1 and matrix[i+1][j]: 
                edge[0] += 1
                dfs(matrix, i+1, j, visited)
            if j < n - 1 and matrix[i][j+1]: 
                edge[0] += 1
                dfs(matrix, i, j+1, visited)
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(grid, i, j, visited)
        return count[0] *4 - edge[0]
            
            
if __name__ == '__main__':
    sol = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    assert sol.islandPerimeter(grid) == 16

    grid = [[0,1]]
    assert sol.islandPerimeter(grid) == 4