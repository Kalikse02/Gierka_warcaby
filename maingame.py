# Author: [Sebastian Kalla]
# Date: [13.01.2025]
# Course: Python I, Lab 3
# Assignment: [Gra - warcaby]
# Description: [Program]
# Version: [Wersja 1.0/nieukończona]
# Dificulty: [Trudne]
# The level of motivation to learn Python: [Wysokie]
# Expected mark: [4]
# Own ideas for modifying tasks, suggestions of your own: […]
# Other notes, own observations: [Nie ma]


import pygame
import sys

BOARD_SIZE = 8
SQUARE_SIZE = 100
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
LINEN = (255, 240, 245)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Warcaby")
clock = pygame.time.Clock()


def draw_text_box(screen, text, x, y, width, height, text_color, box_color):
    pygame.draw.rect(screen, box_color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)


def check_winner(board):
    player1_pieces = 0
    player2_pieces = 0

    for row in board:
        for piece in row:
            if piece in [1, 3]:
                player1_pieces += 1
            elif piece in [2, 4]:
                player2_pieces += 1

    if player1_pieces == 0:
        return 2
    elif player2_pieces == 0:
        return 1
    return 0


def show_winner_screen(screen, winner):
    overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    winner_text = f"Gracz {winner} wygrał!"
    draw_text_box(screen, winner_text,
                  WINDOW_SIZE // 4, WINDOW_SIZE // 3,
                  WINDOW_SIZE // 2, 80,
                  (255, 255, 255), (0, 100, 0))

    draw_text_box(screen, "Kliknij, aby zagrać ponownie",
                  WINDOW_SIZE // 4, WINDOW_SIZE // 2,
                  WINDOW_SIZE // 2, 80,
                  (255, 255, 255), (100, 0, 0))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
    return False


def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece != 0:
                if piece == 1 or piece == 3:
                    color = GREY
                else:
                    color = LINEN

                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, color, center, SQUARE_SIZE // 2 - 10)

                if piece == 3 or piece == 4:
                    pygame.draw.circle(screen, RED, center, SQUARE_SIZE // 2 - 10, 4)

def init_board():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for row in range(3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = 1
    for row in range(5, BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = 2
    return board


def is_valid_move(board, start_pos, end_pos, player):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]

    if board[end_row][end_col] != 0:
        return False

    if piece == 1 or piece == 2:
        direction = 1 if player == 1 else -1
        if end_row - start_row == direction and abs(end_col - start_col) == 1:
            return True
        if end_row - start_row == 2 * direction and abs(end_col - start_col) == 2:
            middle_row = (start_row + end_row) // 2
            middle_col = (start_col + end_col) // 2
            if board[middle_row][middle_col] in [3 - player, 5 - player]:
                return True

    elif piece == 3 or piece == 4:
        if abs(end_row - start_row) == abs(end_col - start_col):
            direction_row = 1 if end_row > start_row else -1
            direction_col = 1 if end_col > start_col else -1

            row, col = start_row + direction_row, start_col + direction_col
            enemy_found = False
            enemy_pos = None

            while row != end_row and col != end_col:
                if board[row][col] != 0:
                    if enemy_found:
                        return False
                    if board[row][col] in [player, player + 2]:
                        return False
                    if board[row][col] in [3 - player, 4 - player]:
                        enemy_found = True
                        enemy_pos = (row, col)
                row += direction_row
                col += direction_col

            return True if not enemy_found else (enemy_found and enemy_pos is not None)

    return False


def make_move(board, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]

    board[end_row][end_col] = piece
    board[start_row][start_col] = 0

    if piece in [3, 4]:
        direction_row = 1 if end_row > start_row else -1
        direction_col = 1 if end_col > start_col else -1
        row, col = start_row + direction_row, start_col + direction_col

        while row != end_row and col != end_col:
            if board[row][col] != 0:
                board[row][col] = 0
            row += direction_row
            col += direction_col

    elif abs(end_row - start_row) == 2:
        middle_row = (start_row + end_row) // 2
        middle_col = (start_col + end_col) // 2
        board[middle_row][middle_col] = 0

    if piece == 1 and end_row == BOARD_SIZE - 1:
        board[end_row][end_col] = 3
    elif piece == 2 and end_row == 0:
        board[end_row][end_col] = 4

def main():
    while True:
        board = init_board()
        selected_piece = None
        player_turn = 1
        game_running = True

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE

                    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                        if selected_piece:
                            if is_valid_move(board, selected_piece, (row, col), player_turn):
                                make_move(board, selected_piece, (row, col))
                                player_turn = 3 - player_turn
                            selected_piece = None
                        elif board[row][col] in [player_turn, player_turn + 2]:
                            selected_piece = (row, col)

            draw_board()
            draw_pieces(board)
            pygame.display.flip()
            clock.tick(FPS)

            winner = check_winner(board)
            if winner != 0:
                if show_winner_screen(screen, winner):
                    break
                else:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()

