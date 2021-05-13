import random
from string import ascii_lowercase as letters

HANGMAN = [
    r"""
   +-----+
   |     |
         |
         |
         |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
         |
         |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
   |     |
         |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
  /|     |
         |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
  /|\    |
         |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
  /|\    |
  /      |
         |
 =========== """,
    r"""
   +-----+
   |     |
   O     |
  /|\    |
  / \    |
         |
 =========== """,
]

riddles = {
    "What is full of holes but still holds water?": "sponge",
    "What is always in front of you but can’t be seen?": "future",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
    "What can you break, even if you never pick it up or touch it?": "promise",
    "What gets wet while drying?": "towel",
    "I shave every day, but my beard stays the same. What am I?": "barber",
    "The more of this there is, the less you see. What is it?": "darkness",
}


def get_random_riddle(riddles):
    return random.choice(riddles.items())


def display_board(HANGMAN, missed_letter, correct_letter, actual_word):
    pass


def get_guess(already_guessed):
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("Please enter a single letter")
        return get_guess(already_guessed)

    elif guess in already_guessed:
        print("Already guessed")
        return get_guess(already_guessed)

    elif guess not in letters:
        print("Please enter a Letter")
        return get_guess(already_guessed)

    return guess


def playagain():
    return input("Would you like to play again (Yes/No)?").lower().startswith("y")


def main():
    pass


if __name__ == "__main__":
    main()
