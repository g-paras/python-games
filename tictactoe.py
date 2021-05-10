from random import randint, choices, choice
from termcolor import colored

# different marker for board to make it look interesting
markers = [
    ("\U0000274C", "\U00002B55"),
    ("\U0001F642", "\U0001F975"),
    ("\U0001F60E", "\U0001F974"),
    ("\U0001F620", "\U0001F608"),
]


def draw_board(board: list) -> None:
    """function to draw tictactoe board"""
    print(*board[:3], sep=" | ")
    print("------------")
    print(*board[3:6], sep=" | ")
    print("------------")
    print(*board[6:], sep=" | ")


def is_board_full(board: list) -> bool:
    """return true if board is full else false"""
    return all(board)


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
    if 0 <= pos <= 8:
        return not board[pos]
    return False


def user_input():
    move = input("Make your move (0-8) ")
    try:
        move = int(move)
    except:
        print("Please enter a valid digit")
        return user_input()
    else:
        if 0 <= move <= 8:
            return move
        print("Your move should be within [0, 8]")
        return user_input()


def make_move(board: list, player: str) -> None:
    pos = user_input()
    if is_free(board, pos):
        pass


def main():
    marker = choice(markers)
    board = choices(marker, k=9)
    draw_board(board)


if __name__ == "__main__":
    # work in progress, not completed yet
    print("Welcome to Tic Tac Toe by Paras Gupta")
    print("Sample board")
    draw_board(range(9))
    main()
