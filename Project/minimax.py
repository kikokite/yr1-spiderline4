from heuristic import *

heuristic = Heuristic()

def minimax(board, depth, current_player, ROW_COUNT, COL_COUNT, player_1, player_2, alpha=float('-inf'), beta=float('inf'), history_table=None):
    if depth == 0 or board.win(player_1) or board.win(player_2) or board.is_full():
        return heuristic.final_heuristic(board, player_1, player_2, ROW_COUNT, COL_COUNT), -1, -1

    maximizing_player = current_player == player_2
    if maximizing_player:
        max_eval = float('-inf')
        best_row = None
        best_col = None

        # Order moves based on history table
        actions = board.actions()
        if history_table:
            actions.sort(key=lambda move: history_table.get(move, 0), reverse=True)

        for r, c in actions:
            new_board = copy.deepcopy(board)
            new_board.put_piece(player_2, r, c)
            eval, _, _ = minimax(new_board, depth - 1, False, ROW_COUNT, COL_COUNT, player_1, player_2, alpha, beta, history_table)
            if eval > max_eval:
                best_row = r
                best_col = c
                max_eval = eval
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        # Update history table
        if history_table and max_eval >= beta:
            history_table[(best_row, best_col)] = depth

        return max_eval, best_row, best_col

    else:
        min_eval = float('inf')
        best_row = None
        best_col = None

        # Order moves based on history table
        actions = board.actions()
        if history_table:
            actions.sort(key=lambda move: history_table.get(move, 0), reverse=True)

        for r, c in actions:
            new_board = copy.deepcopy(board)
            new_board.put_piece(player_1, r, c)
            eval, _, _ = minimax(new_board, depth - 1, True, ROW_COUNT, COL_COUNT, player_1, player_2, alpha, beta, history_table)
            if eval < min_eval:
                best_row = r
                best_col = c
                min_eval = eval
            beta = min(beta, eval)
            if beta <= alpha:
                break

        # Update history table
        if history_table and min_eval <= alpha:
            history_table[(best_row, best_col)] = depth

        return min_eval, best_row, best_col