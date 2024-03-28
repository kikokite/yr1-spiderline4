import pygame
import sys
import numpy as np

# Tamanho tabuleiro
ROW_COUNT = 8
COL_COUNT = 7

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

class Board:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COL_COUNT))
        self.turn = 0  # Player 1 starts
        self.game_over = False
        

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

        #Verificar horizontal
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if (
                    self.board[r][c] == player
                    and self.board[r][c + 1] == player
                    and self.board[r][c + 2] == player
                    and self.board[r][c + 3] == player
                ):
                    return True

        #Verificar vertical
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if (
                    self.board[r][c] == player
                    and self.board[r + 1][c] == player
                    and self.board[r + 2][c] == player
                    and self.board[r + 3][c] == player
                ):
                    return True

        #Verificar diagonal com declive positivo
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (
                    self.board[r][c] == player
                    and self.board[r - 1][c + 1] == player
                    and self.board[r - 2][c + 2] == player
                    and self.board[r - 3][c + 3] == player
                ):
                    return True

        #Verificar diagonal com decline negativo 
        for c in range(COL_COUNT - 3):
            for r in range(3):
                if (
                    self.board[r][c] == player
                    and self.board[r + 1][c + 1] == player
                    and self.board[r + 2][c + 2] == player
                    and self.board[r + 3][c + 3] == player
                ):
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


def draw_board(board):
    screen.fill(GRAY)

    # Desenha o tabuleiro
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            circle_x = col * CELL_SIZE + CELL_SIZE // 2
            circle_y = row * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 2 - 2  # Leave a small gap between circles
            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), radius)

            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)
            
            if board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), radius)

    pygame.display.flip()


def main():
    board = Board()

    while not board.game_over:
        draw_board(board.board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE
                

                if [row, col] in board.actions():

                    board.put_piece(board.turn+1, row, col)
                    
                    if board.win(board.turn + 1):
                        print(f"Player {board.turn + 1} wins!")
                        board.game_over = True


                    if board.is_full():
                        print("The game is a draw!")
                        board.game_over = True
                        break
                        
                    board.turn = 1 - board.turn  # Switch turns
                    print("Array after click:", board.board)

    draw_board(board.board)
    pygame.time.wait(4000)  # Espera um pouco antes de fechar o jogo
    pygame.quit()



if __name__ == "__main__":
    main()
   