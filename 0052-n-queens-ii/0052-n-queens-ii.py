class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==0:
            return 0
        def check_attack(row,col, chess_board):
            for r in range(n):
                for c in range(n):
                    if r == row and c!=col and chess_board[r][c]==1:
                        return False
                    elif abs(c-col)==abs(r-row) and chess_board[r][c]==1 and r!=row and c!=col:
                        return False
                    elif c==col and r!= row and chess_board[r][c] == 1 :
                        return False
            return True
        res = [0]
        chess_board = [[0 for _ in range(n)] for _ in range(n)]

        def mul_board(chess_board, num_r, res):
            if num_r == n:
                res[0] +=1
                return
            for i in range(n):
                chess_board[num_r][i]=1
                if check_attack(num_r, i, chess_board):
                    mul_board(copy.deepcopy(chess_board), num_r+1, res)
                chess_board[num_r][i]=0
        mul_board(chess_board, 0, res)
        return res[0]