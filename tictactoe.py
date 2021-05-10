from random import randint, choices, choice
from termcolor import colored

# different marker for board to make it look interesting
markers = [
    ("\U0000274C", "\U00002B55"),
    ("\U0001F642", "\U0001F975"),
    ("\U0001F60E", "\U0001F974"),
    ("\U0001F620", "\U0001F608"),
]


def welcome():
    print("Welcome to TicTacToe")
    print("Here is a sample board,\nremeber the positions of board")
    draw_board([" 0", "1", "2", " 3", "4", "5", " 6", "7", "8"])


def draw_board(board: list) -> None:
    """function to draw tictactoe board"""
    print(*board[:3], sep=" | ")
    print("------------")
    print(*board[3:6], sep=" | ")
    print("------------")
    print(*board[6:], sep=" | ")


def choose_marker():
    options = choice(markers)
    print("Choose your marker 1.{} 2.{}:".format(*options), end=" ")
    marker = input()
    try:
        marker = int(marker)
    except:
        print("Reply with 1 or 2")
        return choose_marker()
    else:
        if marker in [1, 2]:
            print(f"Your maker is {options[marker-1]}")
            return options if marker == 1 else options[::-1]
        else:
            print("Reply with 1 or 2")
            return choose_marker()


def is_board_full(board: list) -> bool:
    """return true if board is full else false"""
    return all([i != "  " for i in board])


def play_again() -> bool:
    """ask player to play again and return bool accouding to answer"""
    return input("Would you like to play again (Yes/No)? ").lower().startswith("y")


def player_win(board: list, player: str) -> bool:
    """function to check weather player won or not"""
    return (
        (board[0] == board[1] == board[2] == player)
        or (board[3] == board[4] == board[5] == player)
        or (board[6] == board[7] == board[8] == player)
        or (board[0] == board[3] == board[6] == player)
        or (board[1] == board[4] == board[7] == player)
        or (board[2] == board[5] == board[8] == player)
        or (board[0] == board[4] == board[8] == player)
        or (board[2] == board[4] == board[6] == player)
    )


def is_free(board: list, pos: int) -> bool:
    """checks if pos is free or filled"""
    return board[pos] == "  "


def who_first():
    """who will play first"""
    return randint(0, 1)


def user_input(board):
    move = input("Make your move (0-8) ")
    try:
        move = int(move)
        if move in range(9):
            if is_free(board, move):
                return move
            else:
                print("That position is already taken")
                return user_input(board)
        else:
            print("Your move should be in [0, 8]")
            return user_input(board)
    except:
        print("Please enter a valid digit")
        return user_input(board)


def make_move(board: list, player: str, pos: int) -> None:
    """ask user to make move if input is valid then place the marker"""
    board[pos] = player


def board_copy(board):
    """return a shallow copy of board"""
    return board.copy()


def available_positions(board):
    return [i for i in range(9) if board[i] == "  "]


def computer_move(board: list, computer: str, player: str) -> None:

    for i in available_positions(board):
        cboard = board_copy(board)
        make_move(cboard, computer, i)
        if player_win(cboard, computer):
            make_move(board, computer, i)
            print("Computer moved at position {}".format(i))
            return

    for i in available_positions(board):
        cboard = board_copy(board)
        make_move(cboard, player, i)
        if player_win(cboard, player):
            make_move(board, computer, i)
            print("Computer moved at position {}".format(i))
            return

    for i in [0, 2, 6, 8, 4, 1, 3, 5, 7]:
        if is_free(board, i):
            make_move(board, computer, i)
            print("Computer moved at position {}".format(i))
            return


def main():
    welcome()
    board = ["  "] * 9
    (player, computer) = choose_marker()
    turn = who_first()
    if turn == 1:
        print("Computer will make first move")
    else:
        print("You will go first")
    while True:

        if turn == 1:
            computer_move(board, computer, player)
            draw_board(board)
            turn = 0
            if player_win(board, computer):
                print("You loose, computer win")
                break
            elif is_board_full(board):
                print("There is a tie")
                break
        else:
            pos = user_input(board)
            make_move(board, player, pos)
            draw_board(board)
            turn = 1
            if player_win(board, player):
                print("You win, computer loose")
                break
            elif is_board_full(board):
                print("There is a tie")
                break


if __name__ == "__main__":
    main()
