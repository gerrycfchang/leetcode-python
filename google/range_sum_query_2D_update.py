
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        ##initiate a sum array here
        self.matrix = matrix
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        self.sumArray = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                self.add(i, j, matrix[i-1][j-1])

    def add(self, i, j, value):
        a, b = i, j
        while a < len(self.sumArray):
            while b < len(self.sumArray[0]):
                self.sumArray[a][b] += value
                b += b & -b
            a += a & -a
            b = j
    
    def update(self, i, j, value):
        diff = value - self.matrix[i][j]
        self.add(i+1, j+1, diff)
        self.matrix[i][j] = value

    
    def total(self, i, j):
        a, b, total = i, j, 0

        while a > 0:
            while b > 0:
                total += self.sumArray[a][b]
                b -= b & -b
            a -= a & -a
            b = j
        return total


    def sumRegion(self, row1, col1, row2, col2):
        return self.total(row2 + 1, col2 + 1) - self.total(row2 + 1, col1) - \
               self.total(row1, col2+1) + self.total(row1, col1)


if __name__ == '__main__':
    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = NumMatrix(input)
    res = matrix.sumRegion(1, 1, 2, 2)
    assert  res == 28

    matrix.update(1,1,6)
    res = matrix.sumRegion(1, 1, 2, 2)
    assert  res == 29

