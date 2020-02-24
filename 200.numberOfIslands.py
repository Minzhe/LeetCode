# class Solution:
#     def numIslands(self, grid):
#         if len(grid) == 0: return 0
#         m, n, count = len(grid), len(grid[0]), 0
#         directions = [(1,0), (-1,0), (0,1), (0,-1)]
#         def bfs(i, j):
#             Q = [(i,j)]
#             grid[i][j] = '#'
#             while Q:
#                 i, j = Q.pop(0)
#                 for xmove, ymove in directions:
#                     x, y = i + xmove, j + ymove
#                     if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
#                         grid[x][y] = '#' # marked as visited island
#                         Q.append((x,y))

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     count += 1
#                     bfs(i, j)
#                     print(grid)
        
#         return count

class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        islands = 0
    
        def dfs(x, y):
            Q = [(x, y)]
            grid[x][y] = '0'
            while Q:
                x0, y0 = Q.pop()
                for i, j in dirs:
                    x1, y1 = x0 + i, y0 + j
                    if (0 <= x1 < m) and (0 <= y1 < n) and grid[x1][y1] == '1':
                        grid[x1][y1] = '0'
                        Q.append((x1, y1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
                    print(grid)

        return islands

        

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
sol = Solution()
ans = sol.numIslands(grid)
print(ans)