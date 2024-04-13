from heuristic import *

heuristic = Heuristic()

def minimax(board,depth,MaximizingPlayer,ROW_COUNT,COL_COUNT,player_1,player_2):
    if depth==0 or board.win(player_1) or board.win(player_2) or board.isfull():
        return heuristic.final_heuristic(board,player_1,player_2,ROW_COUNT,COL_COUNT),-1,-1
    
    #player2 = max
    if MaximizingPlayer:
        max_eval=float('-inf')
        best_row=None
        best_col=None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r,c] in board.curr_actions:
                    new_board=copy.deepcopy(board)
                    new_board.put_piece(player_2,r,c)
                    eval,_,_= minimax(new_board,depth-1,False,ROW_COUNT,COL_COUNT)
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
                    new_board.put_piece(player_1,r,c)
                    eval,_,_= minimax(new_board,depth-1,True,ROW_COUNT,COL_COUNT)
                    if eval<min_eval:
                        best_row=r
                        best_col=c
                        min_eval=eval
        
        return min_eval,best_row,best_col