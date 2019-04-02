def hasPath(self, maze, start, destination):
    Q = [start]
    m, n = len(maze), len(maze[0])
    move = [(0,1), (0,-1), (1,0), (-1,0)]

    while Q:
        i, j = Q.pop(0)
        maze[i][j] = -1  # visited

        if (i, j) == (destination[0], destination[1]): 
            return True

        for (step_x, step_y) in move:
            x, y = i + step_x, j + step_y
            while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                x, y = x + step_x, y + step_y
            x, y = x - step_x, y - step_y
            if maze[x][y] == 0:     # stop at non-visited point
                Q.append((x,y))
    
    return False
