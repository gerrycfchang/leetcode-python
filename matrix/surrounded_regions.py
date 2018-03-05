
# 130. Surrounded Regions
# 
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X


class Solution(object):
    def solveLoop(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return
        n, queue, res, flip = len(board[0]), [], [], True
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(1, m-1):
            for j in range(1, n-1):         
                if board[i][j] == 'O' and not visited[i][j]:
                    flip = True
                    queue.append([i, j])
                    while len(queue) > 0:
                        pair = queue.pop(0)
                        a, b = pair[0], pair[1]
                        visited[a][b] = True
                        if board[a][b] == 'X':
                            continue
                        res.append([a, b])
                        if a - 1 >= 0 and not visited[a-1][b] and [a-1, b] not in queue: queue.append([a - 1, b])
                        if a + 1 < m  and not visited[a+1][b] and [a+1, b] not in queue: queue.append([a + 1, b])
                        if b - 1 >= 0 and not visited[a][b-1] and [a, b-1] not in queue: queue.append([a, b - 1])
                        if b + 1 < n  and not visited[a][b+1] and [a, b+1] not in queue: queue.append([a, b + 1])
                        if (a == 0 or a == m - 1 or b == 0 or b == n - 1):
                            flip = False                            
                if flip == True:
                    for pair in res:
                        board[pair[0]][pair[1]] = 'X'
                else:
                    for pair in queue:
                        visited[pair[0]][pair[b]] = True                        
                visited[i][j] = True
                del queue[:]
                del res[:]

    def solveRecur(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        flip, res = [True], []
        def dfs(board, i, j, visited, flip):
            m = len(board)
            n = len(board[0])
            if i < 0 or i >=m or j < 0 or j >= n or visited[i][j] or board[i][j] == 'X': return
            visited[i][j] = True
            res.append([i, j])
            
            if board[i][j] == 'O' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                flip[0] = False
                return
            else:
                if i+1 < m  and not visited[i+1][j] and board[i+1][j] == 'O': dfs(board, i + 1, j, visited, flip)
                if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == 'O': dfs(board, i - 1, j, visited, flip)
                if j+1 < n  and not visited[i][j+1] and board[i][j+1] == 'O': dfs(board, i, j + 1, visited, flip)
                if j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == 'O': dfs(board, i, j - 1, visited, flip)
        
        m = len(board)
        if m == 0: return
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'X': visited[i][j] = True
                if not visited[i][j] and board[i][j] == 'O':
                    dfs(board, i, j, visited, flip)
                    if flip[0]:
                        for pair in res:
                            board[pair[0]][pair[1]] = 'X'
                    del res[:]
                    flip[0] = True

if __name__ == '__main__':
    sol = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    exp = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    sol.solveRecur(board)
    assert board == exp

    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X']
    ]
    exp = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X']
    ]
    sol.solveRecur(board)
    assert board == exp

    board = [
        ['X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['O', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'O']
    ]
    exp = [
        ['X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O']
    ]
    sol.solveLoop(board)
    assert board == exp

    board = [
        ['O', 'X', 'X', 'X', 'O'],
        ['X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'O']
    ]
    exp = [
        ['O', 'X', 'X', 'X', 'O'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'O']
    ]
    sol.solveLoop(board)
    assert board == exp

    sol = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    exp = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    sol.solveLoop(board)
    assert board == exp

    board = [
        ['O', 'X', 'X', 'X', 'O'],
        ['X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'O']
    ]
    exp = [
        ['O', 'X', 'X', 'X', 'O'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'O']
    ]
    sol.solveLoop(board)
    assert board == exp

    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    exp =   [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    sol.solveLoop(board)
    assert board == exp

    board = [
            ["O","X","O","O","O","O","O","O","O"],
            ["O","O","O","X","O","O","O","O","X"],
            ["O","X","O","X","O","O","O","O","X"],
            ["O","O","O","O","X","O","O","O","O"],
            ["X","O","O","O","O","O","O","O","X"],
            ["X","X","O","O","X","O","X","O","X"],
            ["O","O","O","X","O","O","O","O","O"],
            ["O","O","O","X","O","O","O","O","O"],
            ["O","O","O","O","O","X","X","O","O"]]
    exp   = [
            ["O","X","O","O","O","O","O","O","O"],
            ["O","O","O","X","O","O","O","O","X"],
            ["O","X","O","X","O","O","O","O","X"],
            ["O","O","O","O","X","O","O","O","O"],
            ["X","O","O","O","O","O","O","O","X"],
            ["X","X","O","O","X","O","X","O","X"],
            ["O","O","O","X","O","O","O","O","O"],
            ["O","O","O","X","O","O","O","O","O"],
            ["O","O","O","O","O","X","X","O","O"]]
    sol.solveLoop(board)
    assert board == exp

    