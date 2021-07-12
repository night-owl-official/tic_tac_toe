def display_board(board_values: list):
    """
    Displays a tic tac toe board.

        Parameters:
            board_values (list): A list of values to insert into the board.
    """

    # Line 1
    print(f" {board_values[6]} | {board_values[7]} | {board_values[8]} ")
    # Line 2
    print("---+---+---")
    # Line 3
    print(f" {board_values[3]} | {board_values[4]} | {board_values[5]} ")
    # Line 4
    print("---+---+---")
    # Line 5
    print(f" {board_values[0]} | {board_values[1]} | {board_values[2]} ")


# The tic tac toe board values
ttt_board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']