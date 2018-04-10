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
        i, j, idx = 0, 0, 0
        while len(res) < m*n:
            visited[i][j] = True
            res.append(matrix[i][j])
            tmpi = i + dirs[idx][0]
            tmpj = j + dirs[idx][1]        
            if tmpi >= 0 and tmpj >= 0 and tmpi < m and tmpj < n and not visited[tmpi][tmpj]:
                i, j = tmpi, tmpj 
            else:
                idx = (idx + 1) % 4
                i, j = dirs[idx][0] + i, dirs[idx][1] + j
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

    matrix =[
        [  1,  2,  3,  4,  5 ],
        [  6,  7,  8,  9, 10 ],
        [ 11, 12, 13, 14, 15 ], 
        [ 16, 17, 18, 19, 20 ]
    ]
    exp = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
    assert sol.spiralOrder(matrix) == exp 