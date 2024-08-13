import random

def initialize_board(rows, cols, mines):
    board = [['-' for _ in range(cols)] for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mines)
    for pos in mine_positions:
        row = pos // cols
        col = pos % cols
        board[row][col] = 'M'
    return board

def explore_cell(board, row, col):
    if board[row][col] == 'M':
        return False
    elif board[row][col] == '-':
        num_mines = count_adjacent_mines(board, row, col)
        board[row][col] = num_mines
        if num_mines == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if (dr, dc) != (0, 0):
                        r, c = row + dr, col + dc
                        if 0 <= r < len(board) and 0 <= c < len(board[0]):
                            explore_cell(board, r, c)
        return True

def flag_cell(board, row, col):
    if board[row][col] == '-':
        board[row][col] = 'F'

def count_adjacent_mines(board, row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (dr, dc) != (0, 0):
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
                    count += 1
    return count

def check_game_over(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def is_win(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def select_move(board):
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            cell = board[i][j]
            if isinstance(cell, int) and cell > 0:
                num = cell
                flagged_neighbors = count_flagged_neighbors(board, i, j)
                hidden_neighbors = count_hidden_neighbors(board, i, j)
                if num - flagged_neighbors == 0:
                    for ni, nj in get_hidden_neighbors(board, i, j):
                        return (ni, nj, 'explore')
                if num - flagged_neighbors == hidden_neighbors:
                    for ni, nj in get_hidden_neighbors(board, i, j):
                        return (ni, nj, 'flag')
    while True:
        i = random.randint(0, rows - 1)
        j = random.randint(0, cols - 1)
        if board[i][j] == '-':
            return (i, j, 'explore')

def count_flagged_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    count = 0
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if board[i][j] == 'F':
                count += 1
    return count

def count_hidden_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    count = 0
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if board[i][j] == '-':
                count += 1
    return count

def get_hidden_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    neighbors = []
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if board[i][j] == '-':
                neighbors.append((i, j))
    return neighbors
