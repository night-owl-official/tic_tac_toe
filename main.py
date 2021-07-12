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


def update_board(new_value: str, at_position: int, board_values: list):
    """
    Updates the board values by setting the given marker at the given position in the list.

        Parameters:
            new_value (str): A value to set on the board (O, X, ' ').
            at_position (int): A position representing one of the available positions on the board (numpad).
            board_values (list): A list for the values currently set on the board.
    """

    # Update the given board value
    board_values[at_position - 1] = new_value


# The tic tac toe board values
ttt_board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
