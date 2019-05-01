class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find all gate
        if len(rooms) != 0:
            starts = []
            m, n = len(rooms), len(rooms[0])
            move = [(0,1), (0,-1), (1,0), (-1,0)]
            for i in range(m):
                for j in range(n):
                    if rooms[i][j] == 0:
                        starts.append((i,j))
            # start updating the shortest distance
            while starts:
                i, j = starts.pop(0)
                for move_x, move_y in move:
                    x, y = i + move_x, j + move_y
                    if 0 <= x < m and 0 <= y < n and (rooms[x][y] > rooms[i][j] + 1): # previously unreachable position
                        rooms[x][y] = rooms[i][j] + 1
                        starts.append((x,y))
