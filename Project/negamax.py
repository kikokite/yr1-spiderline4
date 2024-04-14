from heuristic import *

def negamax(board, depth, current_player, ROW_COUNT, COL_COUNT, player_1, player_2, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.win(player_1) or board.win(player_2) or board.is_full():
        heuristic = Heuristic()
        return heuristic.final_heuristic(board, player_1, player_2, ROW_COUNT, COL_COUNT) * (-1 if current_player == player_1 else 1), -1, -1
    
    max_eval = float('-inf')
    best_col = -1
    best_row = -1

    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if [r, c] in board.actions():
                new_board = copy.deepcopy(board)
                new_board.put_piece(current_player, r, c)
                eval, _, _ = negamax(new_board, depth - 1, player_2 if current_player == player_1 else player_1, ROW_COUNT, COL_COUNT, player_1, player_2, -beta, -alpha)
                eval = -eval  # Invert the evaluation for the current player

                if eval > max_eval:
                    max_eval = eval
                    best_row = r
                    best_col = c
                
                alpha = max(alpha, eval)
                
                if beta <= alpha:
                    break  # Beta cut-off

    return max_eval, best_row, best_col