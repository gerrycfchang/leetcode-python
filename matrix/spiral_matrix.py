# 54. Spiral Matrix
# 
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        res, dirs, m, n = [], [[0, 1],[1, 0],[0, -1],[-1, 0]], len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        while len(res) < m*n:
            for _dir in dirs:
                while i >= 0 and j >= 0 and i < m and j < n and not visited[i][j]:
                    visited[i][j] = True
                    res.append(matrix[i][j])
                    i += _dir[0]
                    j += _dir[1]
                if len(res) == m*n: break
                i -= _dir[0]
                j -= _dir[1]
                visited[i][j] = False
                res.pop()
        return res


if __name__ == '__main__':
    sol = Solution()
    matrix =[
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    assert sol.spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]
    assert sol.spiralOrder([]) == []