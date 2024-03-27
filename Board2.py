import numpy as np
import math
import random

# Tamanho tabuleiro
ROW_COUNT=8
COL_COUNT=8
SQUARE_SIZE=100


class Board:
    
    
    def __init__(self):
        self.board= np.zeros((ROW_COUNT,COL_COUNT))
        self.player=1
        self.acts=[]
    
    
    def put_piece(self,row,col):     #    0<=row<=ROW_COUNT-1   0<=col<=COL_COUNT-1
        if self.valid_move(row,col):
            self.board[row][col]= self.player
            #print(self.board)    
            return True
        #else:
            #print("Invalid move!")
        return False
    
    
    def valid_move(self,row,col):
        j=0
        if self.board[row][col]==0:    
            if row==0 or row==ROW_COUNT-1: return True
            if col==0 or col==COL_COUNT-1: return True
            for i in range(col):  #verificar as peças à esquerda
                if self.board[row][i]==0:
                    j+=1
                    break
            for i in range(col+1,COL_COUNT):  #verificar as peças à direita
                if self.board[row][i]==0:
                    j+=1
                    break
            for i in range(row):  #verificar as peças acima
                if self.board[i][col]==0:
                    j+=1
                    break
            for i in range(row+1,ROW_COUNT):  #verificar as peças abaixo
                if self.board[i][col]==0:
                    j+=1
                    break
        else: return False
        if j==4: return False
        return True
    

    def actions(self): #função que atualiza a lista com todos os movimentos possíveis num determinado momento do jogo
        self.acts=[]
        for i in range (ROW_COUNT):
            for j in range (COL_COUNT):
                if self.valid_move(i,j):
                    self.acts.append([i,j])
        return self.acts



    def win(self):
        for c in range(COL_COUNT-3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == self.player and self.board[r][c+1] == self.player and self.board[r][c+2] == self.player and self.board[r][c+3] == self.player:
                    return True
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == self.player and self.board[r+1][c] == self.player and self.board[r+2][c] == self.player and self.board[r+3][c] == self.player: 
                    return True
        for c in range(COL_COUNT - 3):
            for r in range(3,ROW_COUNT):
                if self.board[r][c] == self.player and self.board[r-1][c+1] == self.player and self.board[r-2][c+2] == self.player and self.board[r-3][c+3] == self.player: 
                    return True
        for c in range(COL_COUNT - 3):
            for r in range(3):
                if self.board[r][c] == self.player and self.board[r+1][c+1] == self.player and self.board[r+2][c+2] == self.player and self.board[r+3][c+3] == self.player: 
                    return True
        return False
    

    def is_full(self):
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT):
                if self.board[r][c]==0:
                    return False
        return True
    

#board=Board()
#print(board.board)
#print("Jogadas no formato: linha coluna (em que 0<=linha<=ROW_COUNT-1 e 0<=coluna<=COL_COUNT-1)")
#while True:
#    board.actions()
#    print(board.acts)
#    print("Vez do jogador", board.player)
#    a,b=map(int,input().split())
#    while board.put_piece(a,b)==False:
#        a,b=map(int,input().split())
#    if board.win():
#        print("Vitória do jogador", board.player)
#        break
#    if board.is_full():
#        print("Empate")
#        break
#    if board.player==1: board.player=2
#    else:
#        board.player=1