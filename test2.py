import pygame
import sys
import numpy as np

# Tamanho tabuleiro
ROW_COUNT = 8
COL_COUNT = 8

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 700, 700
ROWS, COLS = ROW_COUNT, COL_COUNT
CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spider Line 4")

# Define cores
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
GREEN = (0, 255, 0)  # New color for the winning pieces border

class Board:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COL_COUNT))
        self.turn = 0  # Player 1 starts
        self.game_over = False
        self.winning_pieces = []  # List to store winning pieces coordinates

    def put_piece(self, player, row, col):
        if self.valid_move(row, col):
            self.board[row][col] = player
            return True
        else:
            print("Invalid move!")
            return False

    def valid_move(self, row, col):
        check_sides = 0
        if self.board[row][col] == 0:
            if row == 0 or row == ROW_COUNT - 1:
                return True
            if col == 0 or col == COL_COUNT - 1:
                return True
            for i in range(col):  # verificar as peças à esquerda
                if self.board[row][i] == 0:
                    check_sides += 1
                    break
            for i in range(col + 1, COL_COUNT):  # verificar as peças à direita
                if self.board[row][i] == 0:
                    check_sides += 1
                    break
            for i in range(row):  # verificar as peças acima
                if self.board[i][col] == 0:
                    check_sides += 1
                    break
            for i in range(row + 1, ROW_COUNT):  # verificar as peças abaixo
                if self.board[i][col] == 0:
                    check_sides += 1
                    break
        else:
            return False
        if check_sides == 4:
            return False
        return True

    def actions(self):  # função que atualiza a lista com todos os movimentos possíveis num determinado momento do jogo
        self.curr_actions = []
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if self.valid_move(i, j):
                    self.curr_actions.append([i, j])
        return self.curr_actions

    def win(self, player):
        # Verificar horizontal
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if (
                    self.board[r][c] == player
                    and self.board[r][c + 1] == player
                    and self.board[r][c + 2] == player
                    and self.board[r][c + 3] == player
                ):
                    self.winning_pieces = [[r, c], [r, c + 1], [r, c + 2], [r, c + 3]]
                    return True

        # Verificar vertical
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if (
                    self.board[r][c] == player
                    and self.board[r + 1][c] == player
                    and self.board[r + 2][c] == player
                    and self.board[r + 3][c] == player
                ):
                    self.winning_pieces = [[r, c], [r + 1, c], [r + 2, c], [r + 3, c]]
                    return True

        # Verificar diagonal com declive positivo
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (
                    self.board[r][c] == player
                    and self.board[r - 1][c + 1] == player
                    and self.board[r - 2][c + 2] == player
                    and self.board[r - 3][c + 3] == player
                ):
                    self.winning_pieces = [[r, c], [r - 1, c + 1], [r - 2, c + 2], [r - 3, c + 3]]
                    return True

        # Verificar diagonal com declive negativo
        for c in range(COL_COUNT - 3):
            for r in range(3):
                if (
                    self.board[r][c] == player
                    and self.board[r + 1][c + 1] == player
                    and self.board[r + 2][c + 2] == player
                    and self.board[r + 3][c + 3] == player
                ):
                    self.winning_pieces = [[r, c], [r + 1, c + 1], [r + 2, c + 2], [r + 3, c + 3]]
                    return True

        return False

    def is_full(self):
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT):
                if self.board[r][c] == 0:
                    return False
        return True

    def print_board(self):
        print(self.board)


def draw_board(board_obj, hovered_cell):
    screen.fill(GRAY)

    # Desenha o tabuleiro
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            circle_x = col * CELL_SIZE + CELL_SIZE // 2
            circle_y = row * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 2 - 2  # Leave a small gap between circles

            # Check if the current cell is part of the winning pieces
            is_winning_piece = [row, col] in board_obj.winning_pieces

            # Draw the circle
            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), radius)

            # Draw the pieces
            if board_obj.board[row][col] == 1:
                if is_winning_piece:
                    pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)  # Draw red piece
                    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), radius, 3)  # Draw green border for winning pieces
                    
                else:
                    pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)  # Draw red piece
            elif board_obj.board[row][col] == 2:
                if is_winning_piece:
                    pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), radius)  # Draw yellow piece
                    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), radius, 3)  # Draw green border for winning pieces
                    
                else:
                    pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), radius)  # Draw yellow piece

            # Check if the current cell is being hovered over
            if hovered_cell is not None and [row, col] == hovered_cell:
                if board_obj.valid_move(row, col):
                    if board_obj.turn == 0:
                        pygame.draw.circle(screen, RED, (circle_x, circle_y), radius, 3)
                    else:
                        pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), radius, 3)

    pygame.display.flip()




def main():
    board = Board()
    hovered_cell = None

    while not board.game_over:
        draw_board(board, hovered_cell)  # Pass the Board object instead of board.board

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE
                if [row, col] in board.actions():
                    hovered_cell = [row, col]
                else:
                    hovered_cell = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if [row, col] in board.actions():
                    board.put_piece(board.turn + 1, row, col)

                    if board.win(board.turn + 1):
                        print(f"Player {board.turn + 1} wins!")
                        board.game_over = True

                    if board.is_full():
                        print("The game is a draw!")
                        board.game_over = True
                        break

                    board.turn = 1 - board.turn  # Switch turns
                    print("Array after click:", board.board)

    draw_board(board, None)  # Draw the final state without hover effect
    pygame.time.wait(6000)  # Waits a bit before closing the game
    pygame.quit()


if __name__ == "__main__":
    main()
