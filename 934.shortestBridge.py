def shortestBridge(A):
    move = [(0,1), (0,-1), (1,0), (-1,0)]
    m, n = len(A), len(A[0])

    # find the first land of an island
    def find_first_land():
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    return (i, j)
    # find the land of first island
    def find_first_island(i, j):
        A[i][j] = -1    # mark the first island as -1
        island.append((i,j))
        for move_x, move_y in move:
            x, y = i + move_x, j + move_y
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                find_first_island(x, y)

    x, y = find_first_land()
    island = []
    find_first_island(x, y)

    # find the other island
    steps = 0
    while island:
        outer = []
        for i, j in island:
            for move_x, move_y in move:
                x, y = i + move_x, j + move_y
                if 0 <= x < m and 0 <= y < n:
                    if A[x][y] == 1:
                        return steps
                    elif A[x][y] == 0:
                        A[x][y] = -1
                        outer.append((x, y))
        steps += 1
        island, outer = outer, []
    return -1
