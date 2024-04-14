from heuristic import *

heuristic = Heuristic()

def minimax(board,depth,current_player,ROW_COUNT,COL_COUNT,player_1,player_2,alpha=float('-inf'),beta=float('inf')):
    if depth==0 or board.win(player_1) or board.win(player_2) or board.is_full():
        heuristic=Heuristic()
        return heuristic.final_heuristic(board,player_1,player_2,ROW_COUNT,COL_COUNT),-1,-1
    
    MaximizingPlayer= current_player==player_2
    if MaximizingPlayer:
        max_eval=float('-inf')
        best_row=None
        best_col=None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r,c] in board.actions():
                    new_board=copy.deepcopy(board)
                    new_board.put_piece(player_2,r,c)
                    eval,_,_=minimax(new_board,depth-1,False,ROW_COUNT,COL_COUNT,player_1,player_2,alpha,beta)
                    if eval>max_eval:
                        best_row=r
                        best_col=c
                        max_eval=eval
                    alpha=max(alpha,eval)
                    if beta <= alpha:
                        break
        
        return max_eval,best_row,best_col
    
    #player1 = min
    else:
        min_eval=float('inf')
        best_row=None
        best_col=None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r,c] in board.actions():
                    new_board=copy.deepcopy(board)
                    new_board.put_piece(player_1,r,c)
                    eval,_,_=minimax(new_board,depth-1,True,ROW_COUNT,COL_COUNT,player_1,player_2,alpha,beta)
                    if eval<min_eval:
                        best_row=r
                        best_col=c
                        min_eval=eval
                    beta=min(beta,eval)
                    if beta <= alpha:
                        break
        
        return min_eval,best_row,best_col



def negamax(board,depth,current_player,ROW_COUNT,COL_COUNT,player_1,player_2,alpha=float('-inf'),beta=float('inf')):
    if depth==0 or board.win(player_1) or board.win(player_2) or board.is_full():
        heuristic=Heuristic()
        return heuristic.final_heuristic(board,player_1,player_2,ROW_COUNT,COL_COUNT)*(-1 if current_player == 1 else 1),-1,-1
    
    max_eval=float('-inf')
    best_col=-1
    best_row=-1

    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if [r, c] in board.actions():
                new_board = copy.deepcopy(board)
                new_board.put_piece(current_player, r, c)
                eval,_ , _ = negamax(new_board, depth - 1, 1 if current_player == 2 else 2, ROW_COUNT, COL_COUNT, -beta, -alpha)
                eval = -eval  # Inverte o valor da avaliação para o jogador atual
                if eval > max_eval:
                    best_row = r
                    best_col = c
                    max_eval = eval
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
    return max_eval, best_row, best_col