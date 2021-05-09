from random import randint, choices
from termcolor import colored

# different marker for board to make it look interesting
markers = [
    ("\U0000274C", "\U00002B55"),
    ("\U0001F642", "\U0001F975"),
    ("\U0001F60E", "\U0001F974"),
]


def draw_board(board):
    """function to draw tictactoe board"""
    print(*board[:3], sep=" | ")
    print("------------")
    print(*board[3:6], sep=" | ")
    print("------------")
    print(*board[6:], sep=" | ")


def main():
    # board = ["\U0000274C"] * 9
    board = choices([i[0] for i in markers] + [i[1] for i in markers], k=9)
    draw_board(board)


if __name__ == "__main__":
    main()
