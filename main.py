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

        Returns:
            A boolean value holding False when the board can't be updated and True otherwise.
    """

    # The chosen position is available
    if board_values[at_position - 1] == ' ':
        # Update the given board value
        board_values[at_position - 1] = new_value
        return True

    # Board position is already taken
    return False


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
        user_choice = input("Please select a position (1-9): ")

        # User entered a string not convertible into a number
        if not user_choice.isdigit():
            print("*That was not a number!*\n")
            continue

        # At this point, the user entered a number,
        # we can convert the string into an integer
        user_choice = int(user_choice)

        # User entered a number but it wasn't in the correct range
        if user_choice not in range(1, 10):
            print("*The position you entered is not valid!*\n")
            continue

        # At this point, the user entered a valid number
        # we can stop prompting them to enter a number
        is_valid = True

    return user_choice


def set_players_markers(p_data: dict):
    """
    Asks the player 1 what marker they want and sets the markers for both players.

        Parameters:
            p_data (dict): A dictionary for player's data. (It will store markers for both players).
    """

    # Keep looping until the user enters a valid marker
    while True:
        # Store the user's choice in a variable
        p1_choice = input("Player 1, choose your marker (X, O): ")

        # Check if the user's choice is a valid marker
        # we keep this case insensitive
        if p1_choice.lower() not in ['x', 'o']:
            print("*This marker does not exist!*\n")
            continue

        # At this point, the user entered a valid marker
        # we assign the chosen marker to player 1 (uppercase)
        # and the opposite marker goes to player 2 (uppercase as well)
        p_data["p1"] = p1_choice.upper()
        p_data["p2"] = 'O' if (p1_choice.lower() == 'x') else 'X'

        # All the markers have been assigned
        # we can stop the loop
        break


def start_game():
    """
    Contains the game loop and runs the game logic.
    """

    # The tic tac toe board values
    ttt_board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # The player data to hold the markers
    player_data = dict()
    # Flag used to start or stop a new game
    is_playing = True
    # The current player's turn
    player_turn = "p1"

    # Set the player markers
    set_players_markers(player_data)
    # Display the initial state of the board
    display_board(ttt_board_values)

    # Tell the user who is to play now
    print("\nPlayer 1, it's your turn!")

    # Keep the game loop going until the user doesn't want to play anymore
    while is_playing:
        # Ask the current player where they want to place their marker
        # and update the board based on the current player's marker and where
        # they placed it
        board_updated = update_board(player_data[player_turn], get_user_choice(), ttt_board_values)
        # Display the updated board
        display_board(ttt_board_values)

        # When the board couldn't be updated warn the user
        # and prompt them again to enter a position
        if not board_updated:
            print("\n*The chosen position is already taken!*")
            continue

        # Now the next player can place their marker
        # update player's turn
        player_turn = "p1" if (player_turn == "p2") else "p2"
        # Tell the user who is to play now
        player_name = "Player 1" if (player_turn == "p1") else "Player 2"
        print(f"\n{player_name}, it's your turn!")


if __name__ == "__main__":
    # Run the game
    start_game()
