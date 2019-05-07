import copy

class Solution(object):
    def slidingPuzzle(self, board):
        if board == [[1,2,3],[4,5,0]]: return 0
        move = {(0,0): ('up', 'left'), (0,1): ('up', 'left', 'right'), (0,2): ('up', 'right'),
                (1,0): ('down', 'left'), (1,1): ('down', 'left', 'right'), (1,2): ('down', 'right')}

        def findZero(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        return i, j
        
        def slide(board, direction, i, j):
            grid = copy.deepcopy(board)
            if direction == 'left':
                grid[i][j] = grid[i][j+1]
                grid[i][j+1] = 0
                return grid, i, j+1
            if direction == 'right':
                grid[i][j] = grid[i][j-1]
                grid[i][j-1] = 0
                return grid, i, j-1
            if direction == 'up':
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = 0
                return grid, i+1, j
            if direction == 'down':
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = 0
                return grid, i-1, j

        i, j = findZero(board)
        Q = [(board, i, j, 0)]
        seen = []
        while Q:
            grid, i, j, count = Q.pop(0)
            for direction in move[(i,j)]:
                status, x, y = slide(grid, direction, i, j)
                if status == [[1,2,3],[4,5,0]]:
                    return count + 1
                elif status not in seen:
                    seen.append(status)
                    Q.append((status, x, y, count+1))
        return -1
        

board = [[1,2,3],[4,5,0]]
sol = Solution()
ans = sol.slidingPuzzle(board)
print(ans)