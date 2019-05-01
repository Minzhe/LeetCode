class Solution:
    def updateMatrix(self, matrix):
        move = [(0,1), (0,-1), (1,0), (-1,0)]
        starts = [] # all the starting position need to track
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    starts.append((i,j))
                else:
                    matrix[i][j] = float('inf') # mark all 1 as inf
        # update the distance matrix from the start position
        while starts:
            i, j = starts.pop(0)
            for move_x, move_y in move:
                x, y = i + move_x, j + move_y
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] + 1:
                    matrix[x][y] = matrix[i][j] + 1 # update the shortest distance
                    starts.append((x,y))
        return matrix