"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", a
nd in each diagonal all elements are the same, so the answer is True.

"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool

        return all(i == 0 or j == 0 or matrix[i-1][j-1] == val
                   for i, row in enumerate(matrix)
                   for j, val in enumerate(row))
        """
        for i in range (len(matrix[0])):
            if not self.checkDiagonal(matrix, 0, i):
                return False

        for j in range (1, len(matrix)):
            if not self.checkDiagonal(matrix, j, 0):
                return False
        return True

    def checkDiagonal(self, matrix, i, j):
        value = matrix[i][j]
        while i < len(matrix) and j < len(matrix[0]):
            if value != matrix[i][j]:
                return False
            else:
                i += 1
                j += 1
        return True
