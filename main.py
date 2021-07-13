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


def reset_board(board_values: list):
    """
    Resets the board values to be the default ones.

        Parameters:
            board_values (list): A list of the board values.
    """

    # Loop through the board values and set them all to the default value
    for i in range(len(board_values)):
        board_values[i] = ' '


def get_user_choice() -> int:
    """
    Runs until the user inputs a valid choice and returns the latter.

        Returns:
             user_choice (int): A valid choice from the user (a number between 1 and 9).
    """

    user_choice = ""

    # Keep looping until the user enters a valid number
    is_valid = False
    while not is_valid:
        user_choice = input("Please enter a number (1-9): ")

        # User entered a string not convertible into a number
        if not user_choice.isdigit():
            print("*That was not a number!*\n")
            continue

        # At this point, the user entered a number,
        # we can convert the string into an integer
        user_choice = int(user_choice)

        # User entered a number but it wasn't in the correct range
        if user_choice not in range(1, 10):
            print("*The number you entered is not valid!*\n")
            continue

        # At this point, the user entered a valid number
        # we can stop prompting them to enter a number
        is_valid = True

    return user_choice


# The tic tac toe board values
ttt_board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(get_user_choice())
