import time

def display_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()
    time.sleep(1)
