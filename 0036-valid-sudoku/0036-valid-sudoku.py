class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, squares = {}, {}, {} 

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                #NOTE: We can also use a Set to not contain duplicates
                if r not in rows:  
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = set()

                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r// 3, c // 3)].add(board[r][c])

        return True