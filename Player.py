from Mines import initialize_board, explore_cell, flag_cell, check_game_over, is_win, select_move
from Moves import display_board

def minesweeper_game(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    game_over = False
    while not game_over:
        display_board(board)
        i, j, action = select_move(board)
        if action == 'explore':
            move_successful = explore_cell(board, i, j)
            if not move_successful:
                print("Game over! You hit a mine.")
                break
        elif action == 'flag':
            flag_cell(board, i, j)
        game_over = check_game_over(board)
    display_board(board)
    if is_win(board):
        print("Congratulations! You win!")
    else:
        print("Game over. You lose.")

minesweeper_game(10, 10, 10)
