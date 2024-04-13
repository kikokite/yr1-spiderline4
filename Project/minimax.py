from heuristic import *

heuristic = Heuristic()

def Minimax(board, depth, alpha, beta, MaximizingPlayer, ROW_COUNT, COL_COUNT):
    if depth == 0 or board.win(1) or board.win(2) or board.is_full():
        heuristic = Heuristic()
        return heuristic.final_heuristic(board, 1, 2, ROW_COUNT, COL_COUNT), -1, -1

    if MaximizingPlayer:
        max_eval = float('-inf')
        best_row = None
        best_col = None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r, c] in board.actions():
                    new_board = copy.deepcopy(board)
                    new_board.put_piece(1, r, c)
                    eval, _, _ = Minimax(new_board, depth - 1, alpha, beta, False, ROW_COUNT, COL_COUNT)
                    if eval > max_eval:
                        best_row = r
                        best_col = c
                        max_eval = eval
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cut-off
        return max_eval, best_row, best_col

    else:  # Minimizing player
        min_eval = float('inf')
        best_row = None
        best_col = None
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if [r, c] in board.actions():
                    new_board = copy.deepcopy(board)
                    new_board.put_piece(1, r, c)
                    eval, _, _ = Minimax(new_board, depth - 1, alpha, beta, True, ROW_COUNT, COL_COUNT)
                    if eval < min_eval:
                        best_row = r
                        best_col = c
                        min_eval = eval
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return min_eval, best_row, best_col
