import copy
import random 
import numpy as np

from carqueija_update import *


class Heuristic():

    def score_change(self,c1,c2):
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

    def hot_pos(self,board,player_1,player_2,ROW_COUNT,COL_COUNT):
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
        
        score = 0
        for r in range (ROW_COUNT):
            for c in range (COL_COUNT):
                if board[r][c]==player_1: score+=board_score_matrix[r][c]
                elif board[r][c]==player_2: score-=board_score_matrix[r][c]

        return score


    def evaluate_function(self,board,player1,player2,ROW_COUNT,COL_COUNT): #função que permite avaliar a qualidade de uma jogada, avaliando o estado do tabuleiro após essa jogada ser efetuada
        
        score = 0

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
                score+=self.score_change(c1,c2)
                
        
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
                score+=self.score_change(c1,c2)


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
                score+=self.score_change(c1,c2)


        # Verificar diagonal com declive negativo
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT - 3):
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
                score+=self.score_change(c1,c2)
        
        return score     
    
    def final_heuristic(self,board,player_1,player_2,ROW_COUNT,COL_COUNT):
        
            eval_score = self.hot_pos(board,player_1,player_2,ROW_COUNT,COL_COUNT)
            board_score = self.evaluate_function(board,player_1,player_2,ROW_COUNT,COL_COUNT)
            total_score = eval_score + board_score                           
            return total_score
    

def Minimax(board,depth,MaximizingPlayer,ROW_COUNT,COL_COUNT):
    if depth==0 or board.win(player_1) or board.win(player_2) or board.isfull():
        return Heuristic.final_heuristic(board,player_1,player_2,ROW_COUNT,COL_COUNT),-1,-1
    
    #player2 = max
    if MaximizingPlayer:
        max_eval=float('-inf')
        best_row=None
        best_col=None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r,c] in board.curr_actions:
                    new_board=copy.deepcopy(board)
                    new_board.put_piece(2,r,c)
                    eval,_,_=Minimax(new_board,depth-1,False,ROW_COUNT,COL_COUNT)
                    if eval>max_eval:
                        best_row=r
                        best_col=c
                        max_eval=eval
        
        return max_eval,best_row,best_col
    
    else: #player1 = min
        min_eval=float('inf')
        best_row=None
        best_col=None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r,c] in board.curr_actions:
                    new_board=copy.deepcopy(board)
                    new_board.put_piece(2,r,c)
                    eval,_,_=Minimax(new_board,depth-1,True,ROW_COUNT,COL_COUNT)
                    if eval<min_eval:
                        best_row=r
                        best_col=c
                        min_eval=eval
        
        return min_eval,best_row,best_col
    