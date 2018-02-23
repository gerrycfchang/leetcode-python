"""

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                # calculate the number of lives
                live = 0
                for I in range(max(i-1, 0), min(i+2, m)):
                    for J in range(max(j-1,0), min(j+2, n)):
                        # the value of live could be 2, 3 or more, only need to check the last bit
                        live += board[I][J] & 1

                # live is 4 and the cell itself is live or
                # 3 live neighbors
                # mark the cell asl ive
                if (live == 4 and board[i][j]) or live == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

if __name__ == '__main__':
    sol = Solution()