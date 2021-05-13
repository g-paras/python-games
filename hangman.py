import random
from string import ascii_lowercase as letters
import pyfiglet

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
    return random.choice(list(riddles.items()))


def display_board(HANGMAN, missed_letter, correct_letter, actual_word):
    print(HANGMAN[len(missed_letter)])
    print("Missed Letters:", "".join(missed_letter))

    print("Correct Letters: ", end="")
    # for i in actual_word:
    #     if i in correct_letter:
    #         print(i, end="")
    #     else:
    #         print("_", end="")
    # print()

    # or using list comprehension
    print("".join([i if i in correct_letter else "_" for i in actual_word]))


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
    return input("Would you like to play again (Yes/No)? ").lower().startswith("y")


def guessed_all(correct_letter, actual_answer):
    for i in actual_answer:
        if not i in correct_letter:
            return False
    return True


def main():
    pyfiglet.print_figlet("HANGMAN")
    correct_letter = []
    missed_letter = []
    riddle, answer = get_random_riddle(riddles)
    print(riddle)
    while True:
        guess = get_guess(correct_letter + missed_letter)
        if guess in answer:
            correct_letter.append(guess)
        else:
            missed_letter.append(guess)
        display_board(HANGMAN, missed_letter, correct_letter, answer)

        if len(missed_letter) == 6:
            print("Correct answer is", answer)
            print("You lost, better luck next time \U0001F92A")
            if playagain():
                return main()
            return

        elif guessed_all(correct_letter, answer):
            print("Correct answer is", answer)
            print("You got the answer, you won \U0001F973")
            if playagain():
                return main()
            return


if __name__ == "__main__":
    main()
