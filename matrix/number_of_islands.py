# 200. Number of Islands
# 
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is # formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surround# ed # by water. 
# 
# Example 1:
# 
# 11110
# 11010
# 11000
# 00000
# Answer: 1
# 
# Example 2:
# 
# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        def dfs(grid, i, j, visited):
            m = len(grid)
            n = len(grid[0])
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == '0': return
            visited[i][j] = True
            if i + 1 < m and not visited[i + 1][j]  and grid[i+1][j] == '1': dfs(grid, i + 1, j, visited)
            if i - 1 >= 0 and not visited[i - 1][j] and grid[i-1][j] == '1': dfs(grid, i - 1, j, visited)
            if j + 1 < n and not visited[i][j + 1]  and grid[i][j+1] == '1': dfs(grid, i, j + 1, visited)
            if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j-1] == '1': dfs(grid, i, j - 1, visited)
        
        m = len(grid)
        if m == 0: return count
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, i, j, visited)
                    count += 1
        return count
                
                
if __name__ == '__main__':
    sol = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert sol.numIslands(grid) == 1

    grid = [['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
    ]
    assert sol.numIslands(grid) == 3

    grid = []
    assert sol.numIslands(grid) == 0

