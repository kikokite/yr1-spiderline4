import pygame
import sys
import numpy as np
import random

from minimax import * 

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 700
CELL_SIZE = 70  # Adjusted for visual purposes

# Colors
GRAY = (200, 200, 200)
GRAY2 = (72, 73, 75)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Spider Line 4")


class Board:
    def __init__(self, row_count, col_count):
        self.row_count = row_count
        self.col_count = col_count
        self.board = np.zeros((row_count, col_count))
        self.turn = 0
        self.game_over = False
        self.winning_pieces = []

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
            if row == 0 or row == self.row_count - 1:
                return True
            if col == 0 or col == self.col_count - 1:
                return True
            for i in range(col):
                if self.board[row][i] == 0:
                    check_sides += 1
                    break
            for i in range(col + 1, self.col_count):
                if self.board[row][i] == 0:
                    check_sides += 1
                    break
            for i in range(row):
                if self.board[i][col] == 0:
                    check_sides += 1
                    break
            for i in range(row + 1, self.row_count):
                if self.board[i][col] == 0:
                    check_sides += 1
                    break
        else:
            return False
        if check_sides == 4:
            return False
        return True

    def actions(self):
        self.curr_actions = []
        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.valid_move(i, j):
                    self.curr_actions.append([i, j])
        return self.curr_actions

    def win(self, player):
        for c in range(self.col_count - 3):
            for r in range(self.row_count):
                if (
                    self.board[r][c] == player
                    and self.board[r][c + 1] == player
                    and self.board[r][c + 2] == player
                    and self.board[r][c + 3] == player
                ):
                    self.winning_pieces = [[r, c], [r, c + 1], [r, c + 2], [r, c + 3]]
                    return True

        for c in range(self.col_count):
            for r in range(self.row_count - 3):
                if (
                    self.board[r][c] == player
                    and self.board[r + 1][c] == player
                    and self.board[r + 2][c] == player
                    and self.board[r + 3][c] == player
                ):
                    self.winning_pieces = [[r, c], [r + 1, c], [r + 2, c], [r + 3, c]]
                    return True

        for c in range(self.col_count - 3):
            for r in range(3, self.row_count):
                if (
                    self.board[r][c] == player
                    and self.board[r - 1][c + 1] == player
                    and self.board[r - 2][c + 2] == player
                    and self.board[r - 3][c + 3] == player
                ):
                    self.winning_pieces = [[r, c], [r - 1, c + 1], [r - 2, c + 2], [r - 3, c + 3]]
                    return True

        for c in range(self.col_count - 3):
            for r in range(self.row_count - 3):
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
        for c in range(self.col_count):
            for r in range(self.row_count):
                if self.board[r][c] == 0:
                    return False
        return True


def draw_board(board_obj, hovered_cell):
    screen.fill(GRAY2)

    board_width = board_obj.col_count * CELL_SIZE
    board_height = board_obj.row_count * CELL_SIZE

    # Calculate the left and top offsets to center the board
    left_offset = (WINDOW_WIDTH - board_width) // 2
    top_offset = (WINDOW_HEIGHT - board_height) // 2

    for row in range(board_obj.row_count):
        for col in range(board_obj.col_count):
            circle_x = left_offset + col * CELL_SIZE + CELL_SIZE // 2
            circle_y = top_offset + row * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 2 - 2

            is_winning_piece = [row, col] in board_obj.winning_pieces

            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), radius)

            if board_obj.board[row][col] == 1:
                if is_winning_piece:
                    pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)
                    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), radius, 3)
                else:
                    pygame.draw.circle(screen, RED, (circle_x, circle_y), radius)
            elif board_obj.board[row][col] == 2:
                if is_winning_piece:
                    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), radius)
                    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), radius, 3)
                else:
                    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), radius)

            if hovered_cell is not None and [row, col] == hovered_cell:
                if board_obj.valid_move(row, col):
                    if board_obj.turn == 0:
                        pygame.draw.circle(screen, RED, (circle_x, circle_y), radius, 3)
                    else:
                        pygame.draw.circle(screen, BLUE, (circle_x, circle_y), radius, 3)

    pygame.display.flip()


def display_menu():
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.SysFont("consolas", 60)

    title = title_font.render("SpiderLine4", True, BLACK)
    pvp_text = font.render("Player vs Player", True, BLACK)
    pvc_text = font.render("Player vs CPU", True, BLACK)
    cvc_text = font.render("CPU vs CPU", True, BLACK)

    title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
    pvp_rect = pvp_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    pvc_rect = pvc_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
    cvc_rect = cvc_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 120))

    screen.fill(GRAY)
    screen.blit(title, title_rect)
    pygame.draw.rect(screen, BLACK, pvp_rect.inflate(20, 10), 2)
    screen.blit(pvp_text, pvp_rect)
    pygame.draw.rect(screen, BLACK, pvc_rect.inflate(20, 10), 2)
    screen.blit(pvc_text, pvc_rect)
    pygame.draw.rect(screen, BLACK, cvc_rect.inflate(20, 10), 2)
    screen.blit(cvc_text, cvc_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if pvp_rect.collidepoint(mouse_x, mouse_y):
                    return "pvp"
                elif pvc_rect.collidepoint(mouse_x, mouse_y):
                    return "pvc"
                elif cvc_rect.collidepoint(mouse_x, mouse_y):
                    return "cvc"


def display_board_size_menu():
    font = pygame.font.Font(None, 36)
    title = font.render("Choose Board Size", True, BLACK)
    sizes = [10, 9, 8, 7, 6]
    size_texts = [font.render(f"{size}x{size}", True, BLACK) for size in sizes]

    title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
    size_rects = [text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60 * i)) for i, text in enumerate(size_texts)]

    screen.fill(GRAY)
    screen.blit(title, title_rect)
    for text, rect in zip(size_texts, size_rects):
        pygame.draw.rect(screen, BLACK, rect.inflate(30, 15), 2)
        screen.blit(text, rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for size, rect in zip(sizes, size_rects):
                    if rect.collidepoint(mouse_x, mouse_y):
                        return size

def display_difficulty_menu(message):
    font = pygame.font.Font(None, 36)
    title = font.render(message, True, BLACK)
    difficulties = ["Easy", "Medium (Minimax)", "Medium (Negamax)", "Hardcore"]
    difficulty_texts = [font.render(difficulty, True, BLACK) for difficulty in difficulties]

    title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
    difficulty_rects = [text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60 * i)) for i, text in enumerate(difficulty_texts)]

    screen.fill(GRAY)
    screen.blit(title, title_rect)
    for text, rect in zip(difficulty_texts, difficulty_rects):
        pygame.draw.rect(screen, BLACK, rect.inflate(30, 15), 2)
        screen.blit(text, rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for difficulty, rect in zip(difficulties, difficulty_rects):
                    if rect.collidepoint(mouse_x, mouse_y):
                        return difficulty.lower().replace(" ", "_")


def main(mode):
    if mode == "pvp":
        board_size = display_board_size_menu()
        row_count, col_count = board_size, board_size

        board = Board(row_count, col_count)
        hovered_cell = None

        while not board.game_over:
            draw_board(board, hovered_cell)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    col = (mouse_x - (WINDOW_WIDTH - board.col_count * CELL_SIZE) // 2) // CELL_SIZE
                    row = (mouse_y - (WINDOW_HEIGHT - board.row_count * CELL_SIZE) // 2) // CELL_SIZE
                    if 0 <= row < board.row_count and 0 <= col < board.col_count:
                        if [row, col] in board.actions():
                            hovered_cell = [row, col]
                        else:
                            hovered_cell = None
                    else:
                        hovered_cell = None

                elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        col = (mouse_x - (WINDOW_WIDTH - board.col_count * CELL_SIZE) // 2) // CELL_SIZE
                        row = (mouse_y - (WINDOW_HEIGHT - board.row_count * CELL_SIZE) // 2) // CELL_SIZE

                        if [row, col] in board.actions():
                            board.put_piece(board.turn + 1, row, col)

                            if board.win(board.turn + 1):
                                print(f"Player {board.turn + 1} wins!")
                                board.game_over = True

                            if board.is_full():
                                print("The game is a draw!")
                                board.game_over = True
                                break

                            board.turn = 1 - board.turn
                            print("Array after click:\n", board.board)


        draw_board(board, None)
        pygame.time.wait(3000)
        pygame.quit()


    elif mode == "pvc":
        board_size = display_board_size_menu()
        row_count, col_count = board_size, board_size

        board = Board(row_count, col_count)
        hovered_cell = None

        difficulty = display_difficulty_menu("Choose Difficulty")

        while not board.game_over:
            draw_board(board, hovered_cell)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if board.turn == 0:
                    if event.type == pygame.MOUSEMOTION:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        col = (mouse_x - (WINDOW_WIDTH - board.col_count * CELL_SIZE) // 2) // CELL_SIZE
                        row = (mouse_y - (WINDOW_HEIGHT - board.row_count * CELL_SIZE) // 2) // CELL_SIZE
                        if 0 <= row < board.row_count and 0 <= col < board.col_count:
                            if [row, col] in board.actions():
                                hovered_cell = [row, col]
                            else:
                                hovered_cell = None
                        else:
                            hovered_cell = None

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if board.turn == 0:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            col = (mouse_x - (WINDOW_WIDTH - board.col_count * CELL_SIZE) // 2) // CELL_SIZE
                            row = (mouse_y - (WINDOW_HEIGHT - board.row_count * CELL_SIZE) // 2) // CELL_SIZE

                            if [row, col] in board.actions():
                                board.put_piece(board.turn + 1, row, col)

                                if board.win(board.turn + 1):
                                    print(f"Player {board.turn + 1} wins!")
                                    board.game_over = True

                                if board.is_full():
                                    print("The game is a draw!")
                                    board.game_over = True
                                    break

                                board.turn = 1 - board.turn
                                print("Array after click:\n", board.board)
                    
                # CPU's turn
                else:

                    # Define player_1 and player_2 for clarity
                    player_1 = 1
                    player_2 = 2
                    current_player = board.turn + 1  # This adjusts the player number correctly for the Minimax call

                    if difficulty == "easy":
                        row, col = random.choice(board.actions())
                    elif difficulty == "medium_minimax":
                        _,row,col = minimax(board, 5, current_player, row_count, col_count, player_1,player_2)
                        pass
                    elif difficulty == "medium_negamax":
                        # Implement medium difficulty with Negamax
                        pass
                    elif difficulty == "hardcore":
                        # Implement hardcore difficulty
                        pass

                    board.put_piece(board.turn + 1, row, col)

                    if board.win(board.turn + 1):
                        print(f"Player {board.turn + 1} wins!")
                        board.game_over = True

                    if board.is_full():
                        print("The game is a draw!")
                        board.game_over = True
                        break

                    board.turn = 1 - board.turn
                    print("Array after CPU's move:\n", board.board)

        draw_board(board, None)
        pygame.time.wait(3000)
        pygame.quit() 



    elif mode == "cvc":
        board_size = display_board_size_menu()
        row_count, col_count = board_size, board_size

        board = Board(row_count, col_count)
        hovered_cell = None

        difficulty1 = display_difficulty_menu("Choose Difficulty for the 1st algorithm")
        difficulty2 = display_difficulty_menu("Choose Difficulty for 2nd algorithm")

    # Implement CPU vs. CPU logic based on chosen difficulties

    

if __name__ == "__main__":
    mode = display_menu()
    print(mode)
    main(mode)
