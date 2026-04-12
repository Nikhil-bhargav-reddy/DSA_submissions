class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row gets a set
        # each column gets a set
        # each 3*3 grid gets a set. we can do integer dision n//3 to round down the value into its group(0, 1, 2) esentially converting into a 3*3 of 012 vs 012
        rows={}
        cols={}
        grids={}

        for r in range(0,9):
            for c in range(0,9):
                if r not in rows:
                    rows[r]= set()
                if c not in cols:
                    cols[c]= set()
                if (r//3,c//3) not in grids:
                    grids[(r//3,c//3)] = set()
                if board[r][c]=='.':
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in grids[(r//3,c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r//3,c//3)].add(board[r][c])
        return True