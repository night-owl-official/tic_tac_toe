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


def check_win_or_draw(board_values: list, p_data: dict) -> str:
    """
    Checks the board to see if somebody has won the game or if it was a draw.

        Parameters:
            board_values (list): A list of values representing the board.
            p_data (dict): A dictionary holding player's data. (markers associated to each player)

        Returns:
            A string containing the name of the winner if there was one, or draw if it was a draw.
            It can also return an empty string in case it's neither a draw nor a win.
    """

    # Count how many blank spaces there are on the board
    blank_space_count = 0
    for val in board_values:
        if val == ' ':
            blank_space_count += 1

    # More than 4 blank spaces and the game can't be a draw or a win
    if blank_space_count <= 4:
        # Horizontal check
        if (board_values[6] != ' ') and (board_values[6] == board_values[7]) and (board_values[6] == board_values[8]):
            return "Player 1" if (board_values[6] == p_data["p1"]) else "Player 2"
        elif (board_values[3] != ' ') and (board_values[3] == board_values[4]) and (board_values[3] == board_values[5]):
            return "Player 1" if (board_values[3] == p_data["p1"]) else "Player 2"
        elif (board_values[0] != ' ') and (board_values[0] == board_values[1]) and (board_values[0] == board_values[2]):
            return "Player 1" if (board_values[0] == p_data["p1"]) else "Player 2"

        # Vertical check
        if (board_values[6] != ' ') and (board_values[6] == board_values[3]) and (board_values[6] == board_values[0]):
            return "Player 1" if (board_values[6] == p_data["p1"]) else "Player 2"
        elif (board_values[7] != ' ') and (board_values[7] == board_values[4]) and (board_values[7] == board_values[1]):
            return "Player 1" if (board_values[7] == p_data["p1"]) else "Player 2"
        elif (board_values[8] != ' ') and (board_values[8] == board_values[5]) and (board_values[8] == board_values[2]):
            return "Player 1" if (board_values[8] == p_data["p1"]) else "Player 2"

        # Diagonal check
        if (board_values[6] != ' ') and (board_values[6] == board_values[4]) and (board_values[6] == board_values[2]):
            return "Player 1" if (board_values[6] == p_data["p1"]) else "Player 2"
        elif (board_values[8] != ' ') and (board_values[8] == board_values[4]) and (board_values[8] == board_values[0]):
            return "Player 1" if (board_values[8] == p_data["p1"]) else "Player 2"

        # Nobody won yet and there are no blank spaces left
        # the game is a draw
        if blank_space_count == 0:
            return "Draw"

        # Game isn't over yet
        return ""

    # Game isn't over yet
    return ""


def want_to_play_again():
    """
    Asks the user if they want to play again and validate their input.

        Returns:
            A boolean value holding True if they answer yes and False otherwise.
    """

    # Keep asking the user if they want to play again until their answer is valid
    while True:
        user_choice = input("Do you want to play again (Yes/No)? ")

        # Check if the user input is a valid answer (case insensitive)
        # ask for their input again when not a valid answer
        if user_choice.lower() not in ["yes", "no", 'y', 'n']:
            print("*That was not a valid answer!*\n")
            continue

        # At this point, the user input is valid
        # return true if they want to play again
        if user_choice.lower() in ["yes", 'y']:
            return True

        # Return false if they don't want to play again
        return False


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

        # Check if somebody won or for a draw
        winner = check_win_or_draw(ttt_board_values, player_data)
        if winner == "Draw":
            print("\nIt was a draw!")
        elif winner != "":
            print(f"\n{winner} has won the game!")

        # Now the next player can place their marker
        # update player's turn
        player_turn = "p1" if (player_turn == "p2") else "p2"
        # Tell the user who is to play now
        player_name = "Player 1" if (player_turn == "p1") else "Player 2"
        print(f"\n{player_name}, it's your turn!")


if __name__ == "__main__":
    # Run the game
    start_game()
