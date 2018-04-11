# 59. Spiral Matrix II
# 
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        dirs = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        matrix = [[0] * n for _ in range(n)]
        i = j = idx = 0
        num = 1
        while num < n ** 2 + 1:
            matrix[i][j] = num
            num += 1
            tmpi, tmpj = i + dirs[idx][0], j + dirs[idx][1]
            if tmpi >= 0 and tmpj >= 0 and tmpi < n and tmpj < n and matrix[tmpi][tmpj] == 0:
                i, j = tmpi, tmpj
            else:   
                idx = (idx+1) % 4
                i, j = i + dirs[idx][0], j + dirs[idx][1]
        return matrix
        

if __name__ == '__main__':
    sol = Solution()
    exp = [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
        ]
    assert sol.generateMatrix(3) == exp