import numpy as np
import math 
import random

# Game settings
ROW_COUNT = 8
COL_COUNT = 7
SQUARESIZE = 100


class Board:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COL_COUNT))
        self.column_check = np.full(COL_COUNT, ROW_COUNT - 1, dtype=int)
        self.row_check = np.full(ROW_COUNT, COL_COUNT - 1, dtype=int)
        self.game_over = False
        self.turn = 0  # Player 1 starts


    def put_piece_up(self, player , col):
        if self.valid_col(col):
            for i in range(0,ROW_COUNT):
                if self.board[i][col] == 0:
                    self.board[i][col] = player
                    self.column_check[col] -= 1
                    self.row_check[i] -= 1
                    return True
        else:
            print("Invalid move")
            return False


    def put_piece_down(self, player , col):
        if self.valid_col(col):
            for i in range(ROW_COUNT-1, 0, -1):
                if self.board[i][col] == 0:
                    self.board[i][col] = player
                    self.column_check[col] -= 1
                    self.row_check[i] -= 1
                    return True
        else:
            print("Invalid move")
            return False

    

    def put_piece_left(self, player, row):
        if self.valid_row(row):
            for i in range(0, COL_COUNT-1):
                if self.board[row][i] == 0:
                    self.board[row][i] = player
                    self.column_check [i] -= 1
                    self.row_check[row] -= 1
                    return True
        else:
            print("Invalid move")
            return False

    
    def put_piece_right(self, player, row):
        if self.valid_row(row):
            for i in range(COL_COUNT -1, 0, -1):
                if self.board[row][i] == 0:
                    self.board[row][i] = player
                    self.column_check [i] -= 1
                    self.row_check[row] -= 1
                    return True
        else:
            print("Invalid move")
            return False
        

    
        

    def valid_col(self, col):
        if col >= COL_COUNT or col < 0:
            return False
        if self.column_check[col] < 0:
            return False
        return True


    def valid_row(self, row):
        if row >= ROW_COUNT or row < 0:
            return False
        if self.row_check[row] < 0:
            return False
        return True

    
    
    def win(self,player): 

        #Verificar horizontal
        for c in range(COL_COUNT-3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == player and self.board[r][c+1] == player and self.board[r][c+2] == player and self.board[r][c+3] == player:
                    return True

        #Verificar vertical
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == player and self.board[r+1][c] == player and self.board[r+2][c] == player and self.board[r+3][c] == player: 
                    return True
                
        #Verificar diagonal com declive positivo
        for c in range(COL_COUNT - 3):
            for r in range(3,ROW_COUNT):
                if self.board[r][c] == player and self.board[r-1][c+1] == player and self.board[r-2][c+2] == player and self.board[r-3][c+3] == player: 
                    return True 

        #Verificar diagonal com decline negativo 
        for c in range(COL_COUNT - 3):
            for r in range(3):
                if self.board[r][c] == player and self.board[r+1][c+1] == player and self.board[r+2][c+2] == player and self.board[r+3][c+3] == player: 
                    return True
                
        return False 

    def isfull(self):
        return (np.all(self.column_check < 0))

    def print_board(self):
        print(self.board)


board = Board() 

board.put_piece_up(1,3)
board.put_piece_up(1,3)
board.put_piece_up(1,3)
board.put_piece_up(1,3)
board.put_piece_left(1,3)
board.put_piece_left(1,3)
board.put_piece_left(1,3)
board.put_piece_left(1,3)
board.put_piece_left(1,3)
board.put_piece_right(1,3)
board.put_piece_right(1,3)



board.print_board()
print(board.column_check)
print(board.row_check)
print(board.isfull())
print(board.win(1))
print(board.win(2))
