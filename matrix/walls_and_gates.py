# 286. Walls and Gates
# 
# You are given a m x n 2D grid initialized with these three possible values.
# 
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF 
# as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. 
# If it is impossible to reach a gate, it should be filled with INF.
# 
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        def dfs(rooms, i, j, val, dirs):
            m, n = len(rooms), len(rooms[0])            
            if i < 0 or i >= m or j < 0 or j >= n: return
            if rooms[i][j] > val:
                rooms[i][j] = val
                for _dir in dirs:
                    dfs(rooms, i + _dir[0], j + _dir[1], val + 1, dirs)
        # start from empty door
        m, n = len(rooms), len(rooms[0])
        dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    for _dir in dirs:
                        dfs(rooms, i + _dir[0], j + _dir[1], 1, dirs)


if __name__ == '__main__':
    rooms = [
        [float('inf'), -1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), -1],
        [float('inf'), -1, float('inf'), -1],
        [0, -1, float('inf'), float('inf')]
    ]
    exp = [
        [3, -1, 0,  1],
        [2,  2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3,  4]
    ]
    sol = Solution()
    sol.wallsAndGates(rooms)
    assert rooms == exp
