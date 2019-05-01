class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        area = [0]
        def bfs(i, j):
            Q, s = [(i,j)], 0
            while Q:
                i, j = Q.pop(0)
                s += 1
                grid[i][j] = 0
                for movex, movey in directions:
                    x, y = i + movex, j + movey
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 0
                        Q.append((x,y))
            area.append(s)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        return max(area)

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
sol = Solution()
sol.maxAreaOfIsland(grid)