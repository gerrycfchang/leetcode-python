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
        i = j = 0
        num = 1
        while num < n ** 2 + 1:
            for _dir in dirs:
                while i >= 0 and j >= 0 and i < n and j < n and matrix[i][j] == 0:
                    matrix[i][j] = num
                    num += 1
                    i += _dir[0]
                    j += _dir[1]
                if num == n ** 2 + 1: break
                i -= _dir[0]
                j -= _dir[1]
                num -= 1
                matrix[i][j] = 0
        return matrix
        

if __name__ == '__main__':
    sol = Solution()
    exp = [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
        ]
    assert sol.generateMatrix(3) == exp