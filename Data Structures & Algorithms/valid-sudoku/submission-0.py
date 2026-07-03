class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for each row
        for row in board:
            seen = set()
            for n in row:
                if n in seen:
                    return False
                if n != '.':
                    seen.add(n)
        
        # check for each col
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])
        
        # check for each box
        for rowStart in range(0, 9, 3):
            for colStart in range(0, 9, 3):
                seen = set()
                for i in range(rowStart, rowStart+3):
                    for j in range(colStart, colStart+3):
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != '.':
                            seen.add(board[i][j])

        return True