"""

"""

class Solution(object):
    def stairsWalk(self, x):
        x[0][0] = 0

        for i in range(1, len(x)):
            x[0][i] = 1
            x[i][0] = 1

        for i in range(1, len(x)):
            for j in range(1, len(x[0])):
                x[i][j] = x[i][j-1] + x[i-1][j]

if __name__ == '__main__':
    sol = Solution()
    matrix = [[0 for i in range(5)] for j in range(5)]
    sol.stairsWalk(matrix)

    print matrix
