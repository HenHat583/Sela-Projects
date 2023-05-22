import random
import time

board = [" "] * 9


def display_board():
    print(board[0] + "  | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(board[3] + "  | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(board[6] + "  | " + board[7] + " | " + board[8])


def game_over():
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (6, 4, 2)]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]
    if all(space != ' ' for space in board):
        return 'Tie'
    return False


def get_user_input(symbol):
    while True:
        try:
            position = int(input(f"Enter a position from 1 to 9 for {symbol}: ")) - 1
            if position in range(9) and board[position] == " ":
                return position
            else:
                print("Invalid or taken position. Try again: ")
        except ValueError:
            print("Enter only a full number between 1-9. Thanks: ")


def get_bot_input(symbol):
    available_positions = [i for i in range(9) if board[i] == " "]
    if available_positions:
        for i in range(5):
            print("Bot is choosing" + "." * (i % 3 + 1), end="\r")
            time.sleep(0.6)
        #print("Bot is choosing...   ")
        position = random.choice(available_positions)
        return position
    else:
        return None


def the_game():
    play_against_bot = input("Do you want to play against a bot? (y/n): ").lower() == 'y'

    turn = random.choice(["X", "O"])
    winner = False
    display_board()
    while not winner:
        if play_against_bot and turn == 'O':
            position = get_bot_input(turn)
        else:
            position = get_user_input(turn)
        if position is not None:
            board[position] = turn
        winner = game_over()
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        display_board()

    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"CONGRATULATIONS! {winner} WON")

the_game()