# 490 The Maze
# 
# There is a ball in a maze with empty spaces and walls. 
# The ball can go through empty spaces by rolling up, down, left or right, 
# but it won't stop rolling until hitting a wall. 
# When the ball stops, it could choose the next direction.
# 
# Given the ball's start position, the destination and the maze, 
# determine whether the ball could stop at the destination.
# 
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
# You may assume that the borders of the maze are all walls. 
# The start and destination coordinates are represented by row and column indexes.
# 
# Example 1
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)# 

class Solution(object):
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = self.dfs(maze, start[0], start[1], destination, visited)
        return res

    def dfs(self, maze, i, j, dest, visited):
        m, n, res = len(maze), len(maze[0]), False
        if i == dest[0] and j == dest[1]: 
            visited[i][j] = True
            return True
        visited[i][j] = True
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for _dir in dirs:
            x, y = i, j
            while x >=0 and x < m and y >=0 and y < n and maze[x][y] == 0:
                x += _dir[0]
                y -= _dir[1]                
            x -= _dir[0]
            y += _dir[1]
            if not visited[x][y]:
                res |= self.dfs(maze, x, y, dest, visited)            
        return res

if __name__ == '__main__':
    sol = Solution()
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    assert sol.hasPath(maze, [0,4], [4,4]) == True

    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    assert sol.hasPath(maze, [0,4], [3,2]) == False
