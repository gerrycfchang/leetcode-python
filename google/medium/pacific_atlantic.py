"""

# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and
# top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right)
# from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0: return []
        n, result = len(matrix[0]), []
        pacific = [[False] * n for x in range(m)]
        atlantic = [[False] * n for x in range(m)]
        for i in range(m):
            self.dfs(matrix, pacific, float("-inf"), i, 0)
            self.dfs(matrix, atlantic, float("-inf"), i, n - 1)

        for j in range(n):
            self.dfs(matrix, pacific, float("-inf"), 0, j)
            self.dfs(matrix, atlantic, float("-inf"), m - 1, j)

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, matrix, visited, value, i, j):
        m, n = len(matrix), len(matrix[0])
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or matrix[i][j] < value:
            return
        visited[i][j] = True
        self.dfs(matrix, visited, matrix[i][j], i - 1, j)
        self.dfs(matrix, visited, matrix[i][j], i + 1, j)
        self.dfs(matrix, visited, matrix[i][j], i, j - 1)
        self.dfs(matrix, visited, matrix[i][j], i, j + 1)

if __name__ == '__main__':
    sol = Solution()

    matrix = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]

    result = sol.pacificAtlantic(matrix)
    exp = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert (result == exp)