import copy
import random 
import numpy as np

from Board2 import *



def score_change(c1,c2):
    if c2==0:
        if c1==4: return 10000
        elif c1==3: return 100
        elif c1==2: return 10
        elif c1==1: return 1
    if c1==0:
        if c2==4: return -10000
        elif c2==3: return -100
        elif c2==2: return -10
        elif c2==1: return -1 
    return 0

def hot_pos(board,player1,player2,ROW_COUNT,COL_COUNT):
    score=0
    if ROW_COUNT==6:
        board_score_matrix = np.array([
                [3, 4, 6, 6, 4, 3],
                [4, 5, 7, 7, 5, 4],
                [6, 7, 8, 8, 7, 6],
                [6, 7, 8, 8, 7, 6],
                [4, 5, 7, 7, 5, 4],
                [3, 4, 6, 6, 4, 3]
            ])

    elif ROW_COUNT==7:
        board_score_matrix = np.array([
                [3, 4, 5, 7, 5, 4, 3],
                [4, 6, 8, 9, 8, 6, 4],
                [5, 8, 10, 11, 10, 8, 5],
                [7, 9, 11, 12, 11, 9, 7],
                [5, 8, 10, 11, 10, 8, 5],
                [4, 6, 8, 9, 8, 6, 4],
                [3, 4, 5, 7, 5, 4, 3]           
            ])

    elif ROW_COUNT==8:
        board_score_matrix = np.array([
                [3, 4, 5, 7, 7, 5, 4, 3],
                [4, 6, 8, 9, 9, 8, 6, 4],
                [5, 8, 10, 11, 11, 10, 8, 5],
                [7, 9, 11, 12, 12, 11, 9, 7],
                [7, 9, 11, 12, 12, 11, 9, 7],
                [5, 8, 10, 11, 11, 10, 8, 5],
                [4, 6, 8, 9, 9, 8, 6, 4],
                [3, 4, 5, 7, 7, 5, 4, 3],           
            ])

    elif ROW_COUNT==9:
        board_score_matrix = np.array([
                [3, 4, 5, 7, 9, 7, 5, 4, 3],
                [4, 6, 8, 10, 12, 10, 8, 6, 4],
                [5, 8, 11, 13, 14, 13, 11, 8, 5],
                [7, 10, 13, 15, 16, 15, 13, 10, 7],
                [9, 12, 14, 16, 17, 16, 14, 12, 9]
                [7, 10, 13, 15, 16, 15, 13, 10, 7],
                [5, 8, 11, 13, 14, 13, 11, 8, 5],
                [4, 6, 8, 10, 12, 10, 8, 6, 4],
                [3, 4, 5, 7, 9, 7, 5, 4, 3],          
            ])

    elif ROW_COUNT==10:
        board_score_matrix = np.array([
                [3, 4, 5, 7, 9, 9, 7, 5, 4, 3],
                [4, 6, 8, 10, 12, 12, 10, 8, 6, 4],
                [5, 8, 11, 13, 14, 14, 13, 11, 8, 5],
                [7, 10, 13, 15, 16, 16, 15, 13, 10, 7],
                [9, 12, 14, 16, 17, 17, 16, 14, 12, 9]
                [9, 12, 14, 16, 17, 17, 16, 14, 12, 9]
                [7, 10, 13, 15, 16, 16, 15, 13, 10, 7],
                [5, 8, 11, 13, 14, 14, 13, 11, 8, 5],
                [4, 6, 8, 10, 12, 12, 10, 8, 6, 4],
                [3, 4, 5, 7, 9, 9, 7, 5, 4, 3],          
            ])
    
    for r in range (ROW_COUNT):
        for c in range (COL_COUNT):
            if board[r][c]==player1: score+=board_score_matrix[r][c]
            elif board[r][c]==player2: score-=board_score_matrix[r][c]

    return score

def eval(board,player1,player2,ROW_COUNT,COL_COUNT): #função que permite avaliar a qualidade de uma jogada, avaliando o estado do tabuleiro após essa jogada ser efetuada
    score=0

    # Verificar horizontal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            c1=0
            c2=0
            if board.board[r][c] == player1: c1+=1 #número de peças de cada jogador nesses 4 espaços do tabuleiro
            elif board.board[r][c] == player2: c2+=1
            if board.board[r][c + 1] == player1: c1+=1
            elif board.board[r][c + 1] == player2: c2+=1
            if board.board[r][c + 2] == player1: c1+=1
            elif board.board[r][c + 2] == player2: c2+=1
            if board.board[r][c + 3] == player1: c1+=1
            elif board.board[r][c + 3] == player2: c2+=1
            score+=score_change(c1,c2)
            
    
    # Verificar vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            c1=0
            c2=0
            if board.board[r][c] == player1: c1+=1 #número de peças de cada jogador nesses 4 espaços do tabuleiro
            elif board.board[r][c] == player2: c2+=1
            if board.board[r + 1][c] == player1: c1+=1
            elif board.board[r + 1][c] == player2: c2+=1
            if board.board[r + 2][c] == player1: c1+=1
            elif board.board[r + 2][c] == player2: c2+=1
            if board.board[r + 3][c] == player1: c1+=1
            elif board.board[r + 3][c] == player2: c2+=1
            score+=score_change(c1,c2)


    # Verificar diagonal com declive positivo
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            c1=0
            c2=0
            if board.board[r][c] == player1: c1+=1 #número de peças de cada jogador nesses 4 espaços do tabuleiro
            elif board.board[r][c] == player2: c2+=1
            if board.board[r - 1][c + 1] == player1: c1+=1
            elif board.board[r - 1][c + 1] == player2: c2+=1
            if board.board[r - 2][c + 2] == player1: c1+=1
            elif board.board[r - 2][c + 2] == player2: c2+=1
            if board.board[r - 3][c + 3] == player1: c1+=1
            elif board.board[r - 3][c + 3] == player2: c2+=1
            score+=score_change(c1,c2)


    # Verificar diagonal com declive negativo
    for c in range(COL_COUNT - 3):
        for r in range(3):
            c1=0
            c2=0
            if board.board[r][c] == player1: c1+=1 #número de peças de cada jogador nesses 4 espaços do tabuleiro
            elif board.board[r][c] == player2: c2+=1
            if board.board[r + 1][c + 1] == player1: c1+=1
            elif board.board[r + 1][c + 1] == player2: c2+=1
            if board.board[r + 2][c + 2] == player1: c1+=1
            elif board.board[r + 2][c + 2] == player2: c2+=1
            if board.board[r + 3][c + 3] == player1: c1+=1
            elif board.board[r + 3][c + 3] == player2: c2+=1
            score+=score_change(c1,c2)
    
    score+=hot_pos(board.board,player1,player2,ROW_COUNT,COL_COUNT)
    return score     


#def Minimax(board,depth,player,ROW_COUNT): #COL_COUNT=ROW_COUNT
