class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'*n for j in range(n)]
        res = []

        def place_queen(r, col_set, pos_diag, neg_diag):
            if r >= n:
                res.append(board.copy())
                return
            
            for c in range(len(board[r])):
                pos = r + c
                neg = r - c
                if c not in col_set and pos not in pos_diag and neg not in neg_diag:
                    col_set.add(c)
                    pos_diag.add(pos)
                    neg_diag.add(neg)

                    board[r] = '.'*c + 'Q' + '.'*(n-c-1)
                    place_queen(r+1, col_set, pos_diag, neg_diag)

                    board[r] = '.'*n
                    col_set.remove(c)
                    pos_diag.remove(pos)
                    neg_diag.remove(neg)
            return

        place_queen(0, set(), set(), set())
        return res 