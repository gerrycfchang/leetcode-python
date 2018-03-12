# 505. The Maze II
# 
# There is a ball in a maze with empty spaces and walls. 
# The ball can go through empty spaces by rolling up, down, left or right, 
# but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# 
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. 
# The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
# If the ball cannot stop at the destination, return -1.
# 
# The maze is represented by a binary 2D array. 
# 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
# The start and destination coordinates are represented by row and column indexes.
# 

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        m, n, costlist = len(maze), len(maze[0]), []
        visited = [[float('inf') for _ in range(n)] for _ in range(m)]
        res = self.dfs(maze, start[0], start[1], destination, visited, 0, costlist)
        return min(costlist) if res else -1

    def dfs(self, maze, i, j, dest, visited, cost, costlist):
        m, n, res = len(maze), len(maze[0]), False
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]        
        if i == dest[0] and j == dest[1]: 
            costlist.append(cost)
            return True        
        visited[i][j] = cost
        for _dir in dirs:
            x, y, tmpcost = i, j, 0
            while x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == 0:
                x += _dir[0]
                y -= _dir[1]
                tmpcost = tmpcost + abs(_dir[0]) + abs(_dir[1])
            x -= _dir[0]
            y += _dir[1]
            tmpcost = tmpcost - (abs(_dir[0]) + abs(_dir[1]))
            if visited[x][y] > cost + tmpcost:
                tmp = self.dfs(maze, x, y, dest, visited, cost + tmpcost, costlist)
                res |= tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    assert sol.shortestDistance(maze, [0,4], [4,4]) == 12

    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    assert sol.shortestDistance(maze, [0,4], [3,2]) == -1

    maze = [[0,0],[0,0]]
    assert sol.shortestDistance(maze, [0,0], [1,1]) == 2