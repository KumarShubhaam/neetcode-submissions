class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'*n for j in range(n)]
        res = []

        def diagnolValidation(r,c):
            # right - down
            x, y = r+1, c+1
            while x < n and y < n and x >= 0 and y >= 0:
                if board[x][y] == 'Q':
                    return False
                x += 1
                y += 1

            # left - down
            x, y = r+1, c-1
            while x < n and y < n and x >= 0 and y >= 0:
                if board[x][y] == 'Q':
                    return False
                x += 1
                y -= 1

            # right - up
            x, y = r-1, c+1
            while x < n and y < n and x >= 0 and y >= 0:
                if board[x][y] == 'Q':
                    return False
                x -= 1
                y += 1

            # left - up
            x, y = r-1, c-1
            while x < n and y < n and x >= 0 and y >= 0:
                if board[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1
            return True

        def place_queen(r, col_set):
            if r >= n:
                res.append(board.copy())
                return
            
            for c in range(len(board[r])):
                if c not in col_set and diagnolValidation(r,c):
                    col_set.add(c)             
                    board[r] = '.'*c + 'Q' + '.'*(n-c-1)
                    # print('.'*c + 'Q' + '.'*(n-c-1))
                    place_queen(r+1, col_set)
                    board[r] = '.'*n
                    col_set.remove(c)
            return

        place_queen(0, set())
        return res