class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        # find all O not on board
        m, n, = len(board), len(board[0])
        Os = []
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if 1 <= i < m-1 and 1 <= j < n-1:
                    if board[i][j] == 'O':
                        board[i][j] = 'S'
                elif board[i][j] == 'O':
                    Os.append((i,j))
        while Os:
            i, j = Os.pop(0)
            for xmove, ymove in directions:
                x, y = i + xmove, j + ymove
                if 1 <= x < m-1 and 1 <= y < n-1:
                    if board[x][y] == 'S':
                        board[x][y] = 'O'
                        Os.append((x,y))
        for i in range(m):
            for j in range(n):
                if 1 <= i < m-1 and 1 <= j < n-1:
                    if board[i][j] == 'S':
                        board[i][j] = 'X'
        print(board)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
sol.solve(board)