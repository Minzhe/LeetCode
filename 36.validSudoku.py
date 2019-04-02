def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    boxes = {(i,j):[] for i in range(3) for j in range(3)}
    rows = {i:[] for i in range(9)}
    cols = {i:[] for i in range(9)}
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                x = int(board[i][j])
                if not 0 < x < 10:
                    return False
                else:
                    if x in boxes[i//3,j//3]:
                        return False
                    else:
                        boxes[i//3,j//3].append(x)
                    if x in rows[i]:
                        return False
                    else:
                        rows[i].append(x)
                    if x in cols[j]:
                        return False
                    else:
                        cols[j].append(x)
    return True