from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = [(0,-1), (0,1), (1,0), (-1,0)]
        Q = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    Q.append((i,j))
                elif grid[i][j] == 1:
                    grid[i][j] = float('inf')
                else:
                    grid[i][j] = -1
        print(grid)
        
        while Q:
            i, j = Q.pop()
            for movex, movey in adj:
                x, y = i + movex, j + movey
                if 0 <= x <= m-1 and 0 <= y <= n-1 and grid[x][y] > grid[i][j] + 1:
                    grid[x][y] = grid[i][j] + 1
                    Q.appendleft((x,y))
        
        minutes = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == float('inf'):
                    return -1
                elif grid[i][j] > minutes:
                    minutes = grid[i][j]
        
        return minutes
        