"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by

its upper left corner (row1, col1) and lower right corner (row2, col2).

"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        ##initiate a sum array here
        if len(matrix) == 0: return
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        self.sums = [[0 for j in range (n)] for i in range (m)]

        for i in range (1, m):
            for j in range (1, n):
                self.sums[i][j] = self.sums[i][j-1] + matrix[i-1][j-1]

        for i in range (1, m):
            for j in range (1, n):
                self.sums[i][j] += self.sums[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] \
               - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1]



        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':

    """
    input = matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    """
    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = NumMatrix(input)
    assert matrix.sumRegion(1, 1, 2, 2) == 28